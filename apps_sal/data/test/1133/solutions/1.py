# import sys
# sys.stdin = open("cf593a.in")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
words = [input().strip() for _ in range(n)]
words = [(word, set(word)) for word in words]
words = [(word, s) for word, s in words if len(s) <= 2]

best = 0
for c1 in alphabet:
	for c2 in alphabet:
		shere = set([c1, c2])
		best = max(best, sum(len(word) for word, s in words if not (s - shere)))

print(best)
