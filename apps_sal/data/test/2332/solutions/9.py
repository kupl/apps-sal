n, k, m = tuple(map(int, input().split()))

words = input().split()
wtoi = dict()
for i in range(n):
    wtoi[words[i]] = i + 1

costs = list(map(int, input().split()))

for i in range(k):
    words_in_group = list(map(int, input().split()[1:]))
    cost = min([costs[i - 1] for i in words_in_group])
    for w in words_in_group:
        costs[w - 1] = cost

message = list([wtoi[w] for w in input().split()])

cost = sum([costs[i - 1] for i in message])
print(cost)

