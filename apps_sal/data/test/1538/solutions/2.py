n = int(input())
L = list(map(int, input().split()))

freq = {}

for i in L:
	if i not in freq:
		freq[i] = 0
	freq[i] += 1

m = 0

for j in freq:
	if freq[j] > m:
		m = freq[j]

print(m)
