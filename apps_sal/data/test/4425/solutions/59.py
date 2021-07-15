import math
N,K = map(int,input().split())
prob = 0
for i in range(1,N+1):
    win_seq = max(math.ceil(math.log2(K/i)),0)
    prob += (1/2)**win_seq
print(prob/N)
