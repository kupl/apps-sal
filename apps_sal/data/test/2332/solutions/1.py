(n, k, m) = map(int, input().split())
words = input().split()
cost = list(map(int, input().split()))
new_cost = {}
for _k in range(k):
    a = list(map(int, input().split()))[1:]
    c = min((cost[i - 1] for i in a))
    for i in a:
        new_cost[words[i - 1]] = c
text = input().split()
res = 0
for word in text:
    res += new_cost[word]
print(res)
