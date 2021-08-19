(n, k) = map(int, input().split())
price = list(map(int, input().split()))
count = 0
sum = 0
while count < k:
    abc = min(price)
    sum += abc
    price.pop(price.index(abc))
    count += 1
print(sum)
