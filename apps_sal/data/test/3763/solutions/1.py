n = input()
n = int(n)
arr = [0] * n
fact = [0] * 51
a = input().split()
p = input()
p = int(p)

for i in range(n):
	arr[i] = int(a[i])

if n == 1:
	if arr[0] <= p:
		print(1)
	else:
		print(0)
	return

def pre():
	fact[0] = 1
	for i in range(1, 51):
		fact[i] = fact[i - 1] * i

def get(arr, min_sum, max_sum):
	ways = [[0 for i in range(max_sum + 1)] for i in range(len(arr) + 1)]
	ways[0][0] = 1
	for i in range(len(arr)):
		for j in range(i, -1, -1):
			for k in range(max_sum, -1, -1):
				if k + arr[i] <= max_sum:
					ways[j + 1][k + arr[i]] += ways[j][k]

	ans = 0
	counted = 0
	for i in range(0, len(arr) + 1):
		for j in range(min_sum, max_sum + 1):
			ans += fact[i] * fact[n - i - 1] * ways[i][j] * i
			counted += fact[i] * fact[n - i - 1] * ways[i][j]

	return ans, counted

pre()
tot = 0
count = 0
sm = 0
for i in range(n):
	sm += arr[i]
	arr1 = [0] * (n - 1)
	got = 0
	for j in range(n):
		if j == i:
			continue
		arr1[got] = arr[j]
		got += 1
	how_many = get(arr1, max(0, p - arr[i] + 1), p)
	tot += how_many[0]
	count += how_many[1]

def get_div(a, b):	#a / b
	res = a // b
	a %= b
	for i in range(1, 10):
		a = int(a)
		a *= 10
		x = a // b
		x1 = x
		res += pow(10, -i) * x1
		a -= x * b
	return res

if sm <= p:
	print(n)
else:
	print(get_div(tot, fact[n]))

