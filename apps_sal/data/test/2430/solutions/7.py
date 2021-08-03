import sys
N = int(sys.stdin.readline())

H = []

for i in range(N):
    h = int(sys.stdin.readline())
    H.append(h)

ans = H[0] + 1
p = H[0]
for i in range(1, N):
    if(H[i] >= p):
        ans += 1 + (H[i] - p) + 1
        p = H[i]
    else:
        ans += (p - H[i]) + 1 + 1
        p = H[i]
print(ans)
