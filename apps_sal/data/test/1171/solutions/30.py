import bisect
N, K = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = 0

for i in range(1, K + 1):#i個以下取り出し、K - i個以下戻す＃１００
  nownow = 0
  for p in range(i + 1):#[0:i] から [N - i:N]まで取り出さないところを選べる#100
    #[p:p + N - i]を取り出さない
    if i < N:
      now = sorted(V[:p] + V[p + N - i:])
    else:
      now = V
    #print(now, i, p)
    index = bisect.bisect_right(now, 0)
    #index個の負の数がある。
    if K - i >= index:
      nownow = sum(now[index:])
    else:
      nownow = sum(now[K - i:])
    ans = max(ans, nownow)
    #print(now, nownow, ans)

print(ans)      

