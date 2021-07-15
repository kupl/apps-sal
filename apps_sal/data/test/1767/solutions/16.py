3

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# n = 5
# a = [1,2,4,3,2]
# b = [2,3,3,12,1]

def f(x, l, r):
	res = 0
	for i in range(l, r+1):
		res |= x[i]
	return res

t = [None]*n
sum_a = 0
sum_b = 0
max_sum = 0
for i in range(n):
	sum_a |= a[i]
	sum_b |= b[i]
	t[i] = sum_a + sum_b

	max_sum = max(max_sum, t[i])

print(max_sum)

