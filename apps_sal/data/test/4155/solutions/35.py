N = int(input())
H = list(map(int, input().split()))
active = 0
ans = 0
for i in range(N):
    if H[i] >= active:
        ans += H[i] - active
        active = H[i]
    else:
        active = H[i]
print(ans)
