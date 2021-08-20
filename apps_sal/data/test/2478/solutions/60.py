n = int(input())
N = input()
L = 0
R = 0
num = 0
for c in N:
    if c == '(':
        num += 1
    elif num:
        num -= 1
    else:
        L += 1
R = num
print('(' * L + N + ')' * R)
