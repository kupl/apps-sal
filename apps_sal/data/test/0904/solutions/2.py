import string
n = int(input())
t = input().split(' ')

result = 0

for item in t:
    current = 0
    for letter in item:
        if letter in string.ascii_uppercase:
            current += 1
    result = max(result, current)
print(result)
