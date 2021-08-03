n, d = map(int, input().split())
A = list(map(int, input().split()))
d = d + 1
B = []
for q in range(101):
    B.append(0)
for q in range(n):
    B[A[q]] += 1
# print(*B);
res = 0
for q in range(d):
    res = res + B[q]
# print(res);
ans = res
for q in range(d, 101):
    res = res + B[q] - B[q - d]
    ans = max(res, ans)
print(n - ans)
