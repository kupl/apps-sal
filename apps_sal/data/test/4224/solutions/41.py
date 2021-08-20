N = int(input())
H = list(map(int, input().split()))
ans = 0
for i in range(N):
    while H[i] % 2 == 0:
        ans += 1
        H[i] //= 2
print(ans)
