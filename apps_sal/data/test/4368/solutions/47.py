# 整数NをK進数で表したとき、何桁になるかを求めてください。

N,K = map(int,input().split())

i = 0
while N > 0:
    N = N // K
    i += 1

print(i)
