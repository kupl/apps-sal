#ABC161
N,K=map(int,input().split())
N_new=N%K
print(min(N_new,K-N_new))
