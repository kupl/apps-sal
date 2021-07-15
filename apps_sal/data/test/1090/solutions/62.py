N,K = map(int,input().split())
S = input()
if N == 1:
    print(0)
    return

ans = 0
cnt = 0
for i in range(len(S)-1):
    if S[i] == S[i + 1]:
        ans += 1
    else:
        cnt += 1

ans += min(K,cnt//2) * 2

if K > cnt//2 and S[0] != S[-1]:
    ans += 1

print(ans)
