(n, t, c) = map(int, input().split())
A = map(int, input().split())
B = [0]
for i in A:
    if i > t and B[-1] != 0:
        B.append(0)
    elif i <= t:
        B[-1] += 1
res = 0
for i in B:
    res += 0 if i - c + 1 < 0 else i - c + 1
print(res)
