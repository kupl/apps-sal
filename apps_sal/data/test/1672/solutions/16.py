n = int(input())

str = input()

LAST = str[1]
S = 1
n -= 1

while n > 0:
    str = input()
    if str[0] == LAST:
        S += 1
        LAST = str[1]
    n -= 1

print(S)
