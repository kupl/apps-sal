N = int(input())
H = list(map(int, input().split()))
ans = H[0]
for i in range(N-1):
    if H[i] < H[i+1]:
        ans += H[i+1]-H[i]
print(ans)
