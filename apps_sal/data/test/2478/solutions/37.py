N = int(input())
S = input()
A = 0
B = 0
for s in S:
    if s == '(':
        A += 1
    elif s == ')' and A > 0:
        A -= 1
    else:
        B += 1
print('(' * B + S + ')' * A)
