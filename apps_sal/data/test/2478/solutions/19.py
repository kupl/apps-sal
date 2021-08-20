N = int(input())
S = input()
l = 0
r = 0
for s in S:
    if s == '(':
        r += 1
    elif r > 0:
        r -= 1
    else:
        l += 1
ans = ''.join(['(' * l, S, ')' * r])
print(ans)
