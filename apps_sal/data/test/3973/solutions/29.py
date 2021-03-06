import sys
input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


mod = 10 ** 9 + 7
'\nxを決めればO(N)で答えが求まる.\n全部は求められない.\nxを変更したときの差分に注目.\n\n\naからbへ\n順送りだけのとき,(b-a)%M\nお気に入りを使うとき,1 + (b-x)%M\n\n目標地点がxだった場合，お気に入りを+1すると一気に(b-a)%M-1回必要になる\n元々お気に入りを使うケース(a<x<bみたいな)では-1\nそれ以外なら変化なし\n\n目標地点の値は普通に数える\nお気に入りを使うケースはimosで.区間(a,b)に+1する感じ.\na>bの場合,(0,b)と(a,N]に+1かな\n'
(N, M) = MI()
A = LI()
S = [0] * (M + 3)
prev = [[] for _ in range(M + 1)]
for i in range(N - 1):
    b = A[i + 1]
    a = A[i]
    prev[b].append(a)
    if b > a:
        S[a + 1] += 1
        S[b] -= 1
    elif a > b:
        S[1] += 1
        S[b] -= 1
        S[a + 1] += 1
        S[-1] -= 1
for i in range(M - 1):
    S[i + 1] += S[i]
ans = 0
x = 1
now = A[0]
for i in range(1, N):
    nxt = A[i]
    if nxt > now:
        ans += nxt - now
    else:
        ans += nxt
    now = nxt
temp = ans
for x in range(1, max(A)):
    for p in prev[x]:
        temp += (x - p) % M - 1
    temp -= S[x]
    ans = min(ans, temp)
print(ans)
