n = int(input())
A = list(map(int, input().split()))

ans = 0
find = 1
for i in range(n):

    if A[i] == find:
        find += 1
    else:
        ans += 1


if find == 1:
    ans = -1
print(ans)
