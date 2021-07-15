S, C = map(int, input().split())

ans = min(S, C // 2)
S -= ans
C -= ans * 2
if C >= 4:
    ans += C // 4
print(ans)
