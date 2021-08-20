N = int(input())
A = {}
for i in range(N):
    val = int(input())
    if val in A:
        A[val] += 1
    else:
        A[val] = 1
ans = 0
for (k, v) in A.items():
    if v % 2 != 0:
        ans += 1
print(ans)
