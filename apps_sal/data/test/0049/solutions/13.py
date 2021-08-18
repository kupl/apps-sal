"""
Strategy: Split sequence into subsequences
according to number of digits. Then find corresponding
number and digit in that number.
"""

k = int(input())

num_digits = 1
num_numbers = 9

k -= 1
while k > num_digits * num_numbers:
    k -= num_numbers * num_digits
    num_digits += 1
    num_numbers *= 10

number = 10**(num_digits - 1) + k // num_digits
index = k % num_digits
answer = str(number)[index]
print(answer)
