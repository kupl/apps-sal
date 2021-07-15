N, K = map(int, input().split())
S = input()

s = []
cnt = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        s.append(cnt)
        cnt = 1
s.append(cnt)

ans = 0
if S[0] == '0':
    s = [0] + s
if S[-1] == '0':
    s = s + [0]

if 2*K + 1 > len(s):
    print(sum(s))
    return

s_cumsum = [s[0]] * len(s)
for i in range(1, len(s)):
    s_cumsum[i] = s_cumsum[i-1] + s[i]
    
for i in range(0, len(s), 2):
    if i + 2*K >= len(s):
        break
    if i < 1:
        ans = s_cumsum[i+2*K]
    ans = max(ans, s_cumsum[i+2*K]-s_cumsum[i-1])
    #ans = max(ans, sum(s[i:i+2*K+1]))

print(ans)
