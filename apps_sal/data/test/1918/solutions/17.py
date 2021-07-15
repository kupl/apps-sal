from sys import stdin
import operator

N = int(stdin.readline())

p = list(map(int, stdin.readline().strip().split(" ")))
teams = list([1 if x == "B" else -1 for x in stdin.readline().strip()])

values = list(map(operator.mul, p, teams))

start = sum([x for x in values if max(x, 0)])
# print(start)

total = start
best = start
for i in values:
	total -= i
	best = max(total, best)

total = start
for i in reversed(values):
	total -= i
	best = max(total, best)

# print(p, teams, values, best)
print(best)

