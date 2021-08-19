N = int(input())
*H, = map(int, input().split())
L = len(H)

ans = 0
active = 0

for i in range(N):
    if H[i] <= active:  # 低くなってしまった
        active = H[i]
    else:  # 同じかそれ以上
        ans += H[i] - active
        active = H[i]
print(ans)
