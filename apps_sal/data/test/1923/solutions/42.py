N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)

ans = 0
for i in range(1, 2 * N, 2):
    ans += L[i]

print(ans)
