n, m = list(map(int, input().split()))

a = list(map(int, input().split()))

a.insert(0, 0)
a.append(m)

n += 2

prev = [0]*n

for i in range(1, n, 2):
	prev[i] = a[i] - a[i-1]

# print(a)

for i in range(1, n):
	prev[i] = prev[i-1] + prev[i]

# print(prev)


flip = [0]*n

for i in range(1, n):
	j = n-1-i
	if (j%2 != 0):
			flip[j] = a[j+1] - a[j]

for i in range(1,n):
	j = n-1-i
	flip[j] = flip[j] + flip[j+1]

# print(flip)

print(max(prev[-1], max(prev[i] + flip[i+1] + abs(a[i+1] - a[i] - 1) for i in range(n-1))))
