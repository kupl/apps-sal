n, k, m = map(int, input().split())
word = input().split()
cost = list(map(int, input().split()))
for i in range(k):
    arr = list(map(int, input().split()))
    m = cost[arr[1] - 1]
    for j in range(1, len(arr)):
        if cost[arr[j] - 1] < m:
            m = cost[arr[j] - 1]
    for j in range(1, len(arr)):
        cost[arr[j] - 1] = m
d = {word[i]: cost[i] for i in range(len(word))}
message = input().split()
price = 0
for i in message:
    price = price + d[i]
print(price)
