N = int(input())
A = list(map(int, input().split()))

ans = [0] * (max(A) + 2)

for a in A:
    if a == 0:
        ans[a] += 1
        ans[a + 1] += 1
    if a != 0:
        ans[a - 1] += 1
        ans[a] += 1
        ans[a + 1] += 1
print(max(ans))
