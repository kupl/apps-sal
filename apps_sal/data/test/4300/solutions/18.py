# l,r,d =map(int, input().split()))
n = int(input())
d = list(map(int, input().split()))

# s = [map(int, input()) for i in range(3)]
ans = 0

for i in range(0, n):

    for j in range(i + 1, n):

        ans += d[i] * d[j]

print(ans)
