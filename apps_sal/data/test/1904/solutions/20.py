n = int(input())
s = input()
a = list(map(int, input().split()))
hard = {'h': 1, 'a': 2, 'r': 3, 'd': 4}
cost = [10 ** 20, 0, 0, 0, 0]
for (ai, c) in zip(a, s):
    if c in hard:
        cost[hard[c]] = min(cost[hard[c] - 1], cost[hard[c]] + ai)
print(cost[4])
