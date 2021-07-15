S, C = list(map(int, input().split()))
ans = 0

# 初期のSで可能な限りSCCを作る
if S*2 <= C:
    C = C - S*2
    ans += S
    ans += C // 4
else:
    ans += C // 2

print((int(ans)))

