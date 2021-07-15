n, k = map(int, input().split())

a = list(map(int, input().split()))

s = [0 for i in range(k)]

for i in range(len(a)):	s[i % k] += a[i]

j = 0
for i in range(k):
	if s[i] < s[j]: j = i

print(j + 1)
