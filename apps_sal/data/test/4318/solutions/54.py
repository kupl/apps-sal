N = int(input())
H = list(map(int, input().split()))
maxi = 0
ans = 0
for i in range(N):
    if H[i] >= maxi:
        ans += 1
        maxi = H[i]
print(ans)
