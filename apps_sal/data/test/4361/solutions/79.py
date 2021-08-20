(N, K) = map(int, input().split())
h = [int(input()) for i in range(N)]
s_h = sorted(h)
tmp = []
ans1 = 0
ans2 = 0
ans3 = 0
for i in range(N - K + 1):
    ans1 = s_h[i + K - 1]
    ans2 = s_h[i]
    ans3 = ans1 - ans2
    tmp.append(ans3)
print(min(tmp))
