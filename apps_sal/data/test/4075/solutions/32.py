3
#coding: utf-8

N, M = (int(x) for x in input().split())

S = []
for i in range(M):
    S.append([int(x) - 1 for x in input().split()][1:])
P = [int(x) for x in input().split()]

ret = 0
for bit in range(2**N):
    on = [i for i in range(N) if bit & (1 << i)]
    if all(sum(1 for switch in S[i] if switch in on) % 2 == P[i] for i in range(M)):
        ret += 1
print(ret)
