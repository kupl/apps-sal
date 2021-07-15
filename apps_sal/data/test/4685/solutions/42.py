N_List = list(map(int,input().split()))
N = int(input())
maxN = max(N_List)
print(sum(N_List)-maxN+maxN*(2**N))
