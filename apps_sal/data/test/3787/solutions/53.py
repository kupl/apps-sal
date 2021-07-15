import sys
input = sys.stdin.readline

"""
n-増大列、m-減少列まで　-> 長さ nm 以下であることを示す。帰納法。
(n+1)m + 1 項があるとする。(n+2増大 or m+1減少)の存在をいう。
A：左 nm 項 B：右 m+1 項
Aに1項加えると、(n+1,m+1)のどちらかができる。(n+1)-増大ができるとしてよい。
Bの各項 b に対して、bで終わる(n+1)-増大列が存在する。
Bの中に2-増大列があれば(n+2)増大列ができる。そうでなければBが(m+1)-減少列なのでよい

"""

N,A,B = map(int,input().split())

if A+B-1 > N:
    print(-1)
    return
if A*B < N:
    print(-1)
    return

# 減少列をA個並べる

if B == 1:
    size = [1] * A
else:
    q,r = divmod(N-A,B-1)
    if q < A:
        size = [B] * q + [1+r] + [1] * (A-q-1)
    else:
        size = [B] * A

answer = []
start = 1
for s in size:
    end = start + s
    answer += list(range(end-1, start-1, -1))
    start = end
print(*answer)
