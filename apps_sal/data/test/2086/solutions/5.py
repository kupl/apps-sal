n = int(input())
arr = list(map(int, input().split()))
s, f = list(map(int, input().split()))

num = 0
for i in range(s - 1, f - 1):
	num += arr[i]

t = 0
current = num
for time in range(n):
	current = current - arr[(s - 1 + time) % n] + arr[(f - 1 + time) % n]
	if (current >= num):
		num = current
		t = time

print(n - t)

