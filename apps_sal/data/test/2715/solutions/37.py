K = int(input())
if K >= 50:
    N = 50
    wari = K // N - 1
    amari = K % N
    l = [(50 + wari) + 1] * amari + [(50 + wari) - amari] * (N - amari)
if 50 > K > 1:
    N = K
    l = [K] * K
if K == 1:
    N = 2
    l = [0, 2]
if K == 0:
    N = 2
    l = [1, 1]
##
print(N)
print(*l)
