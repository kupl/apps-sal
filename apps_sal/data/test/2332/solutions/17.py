from sys import stdin
(words, groups, n) = map(int, stdin.readline().split())
words = stdin.readline().split()
price = dict()
pr = list(map(int, stdin.readline().split()))
for i in range(len(words)):
    price[words[i]] = pr[i]
for i in range(groups):
    group = list(map(int, stdin.readline().split()))[1:]
    minpr = 10 ** 18
    for elem in group:
        minpr = min(minpr, price[words[elem - 1]])
    for elem in group:
        price[words[elem - 1]] = minpr
mess = stdin.readline().split()
res = 0
for elem in mess:
    res += price[elem]
print(res)
