"""
Strategy: Split sequence into subsequences
according to number of digits. Then find corresponding
number and digit in that number.
"""

# Standard input.
k = int(input())

# Initilize sequence
num_digits = 1
num_numbers = 9

k -= 1
while k > num_digits * num_numbers:
    # Move sequence starting point.
    k -= num_numbers * num_digits
    num_digits += 1
    num_numbers *= 10

# Generate number.
number = 10**(num_digits - 1) + k // num_digits
# Find index in that number
index = k % num_digits
answer = str(number)[index]
print(answer)
