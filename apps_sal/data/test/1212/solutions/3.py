N, K = input().split()
N, K = int(N), int(K)
planks = tuple(map(int, input().split()))
min_poss = 999999999
sum_array = sorted(planks)
sum_array[K-1] = sum(planks[:K])
for i in range(K,N):
    sum_array[i] = cur = sum_array[i-1]+planks[i]-planks[i-K]
print(sum_array.index(min(sum_array[K-1:]))-K + 2)

