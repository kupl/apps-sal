x, n = [int(x) for x in input().split()]
prime = set()
arr = 1
y = int(x**0.5)
for i in range(2, y + 1):
    while x % i == 0:
        prime.add(i)
        x //= i
if x != 1:
    prime.add(x)
dic = {}
for item in prime:
    dic[item] = 0
for item in prime:
    for i in range(1, 60):
        dic[item] += n // (item**i)
for item in dic:
    arr *= pow(item, dic[item], (10**9 + 7))
print(arr % (10**9 + 7))
