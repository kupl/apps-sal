str = input().split('+')
str.sort()
for r in range(len(str) - 1):
    print(str[r], end='')
    print('+', end='')
print(str[len(str) - 1])
