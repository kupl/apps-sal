N, Q = map(int, input().split())
S = input()


cum_sum = [0] * N
count_AC = [0] * N

for i in range(N-1):
    if (S[i] + S[i+1]) == "AC":

        count_AC[i+1] = 2
        cum_sum[i+1] = 2
    cum_sum[i+1] = cum_sum[i] + cum_sum[i+1]


for _ in range(Q):
    l,r = map(int, input().split())
    l = l - 1
    r = r - 1
    print((cum_sum[r]//2)-(cum_sum[l]//2))   
