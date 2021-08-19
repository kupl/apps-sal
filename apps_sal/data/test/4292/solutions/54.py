(N, K) = map(int, input().split())
price = list(map(int, input().split()))
price.sort()
sum = 0
for i in range(K):
    sum += price[i]
print(sum)
