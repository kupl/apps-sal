import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


mod = 10**9 + 7


"""
xを決めればO(N)で答えが求まる.
全部は求められない.
xを変更したときの差分に注目.


aからbへ
順送りだけのとき,(b-a)%M
お気に入りを使うとき,1 + (b-x)%M

目標地点がxだった場合，お気に入りを+1すると一気に(b-a)%M-1回必要になる
元々お気に入りを使うケース(a<x<bみたいな)では-1
それ以外なら変化なし

目標地点の値は普通に数える
お気に入りを使うケースはimosで.区間(a,b)に+1する感じ.
a>bの場合,(0,b)と(a,N]に+1かな
"""

N, M = MI()
A = LI()

S = [0] * (M + 3)

prev = [[]for _ in range(M + 1)]
for i in range(N - 1):
    # 直前の数字
    b = A[i + 1]
    a = A[i]
    prev[b].append(a)

    # imos
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

# print(1,ans)
temp = ans
for x in range(1, max(A)):
    for p in prev[x]:
        temp += (x - p) % M - 1
    temp -= S[x]
    # print(x+1,temp)
    ans = min(ans, temp)

print(ans)

# print(S)
# print(prev)
