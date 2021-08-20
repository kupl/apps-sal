n = int(input())
S = 0
while n > 0:
    str = input()
    if str[1] == '+':
        S += 1
    else:
        S -= 1
    n -= 1
print(S)
