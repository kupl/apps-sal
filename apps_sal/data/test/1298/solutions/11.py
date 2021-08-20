n = int(input())
str = input()
zero = 0
one = 0
for char in str:
    if char == '0':
        zero += 1
    else:
        one += 1
count = min(zero, one)
print(n - count * 2)
