n = int(input())
ans = 0
A = sorted(list(map(int, input().split())))[::-1]
for i in range(n):
    if i % 2 == 0:
        ans += A[i]
    else:
        ans -= A[i]
print(ans)
