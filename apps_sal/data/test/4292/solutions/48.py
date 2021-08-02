import itertools
[N, K] = [int(i) for i in input().split()]
price = [int(i) for i in input().split()]
price.sort()
sum = 0
for i in range(K):
    sum += price[i]
print(sum)
