N = int(input())
A = list(map(int, input().split()))

if 1 not in A:
    ans = -1
else:
    now = 1
    ans = 0
    for i in range(N):
        if A[i] == now:
            now += 1
        else:
            ans += 1

print(ans)
