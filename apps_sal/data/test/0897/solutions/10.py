n, m = list(map(int, input().split(" ")))
s1 = list(map(int, input().split(" ")))
s2 = list(map(int, input().split(" ")))

N = 10 ** 9 + 7
res = True
inv = pow(m, N - 2, N)
cur = 1
result = 0
inv_2 = pow(2, N - 2, N)

for i in range(n):
	if s1[i] == 0 and s2[i] == 0:
		result = (result + cur * inv_2  * (N + 1 - inv)) % N
		cur = (cur * inv) % N 
		continue

	if s1[i] == 0:
		cur = (cur * inv) % N 
		result = (result + (m - s2[i]) * cur) % N
		continue

	if s2[i] == 0:
		cur = (cur * inv) % N
		result = (result + (s1[i] - 1) * cur) % N
		continue

	if s1[i] < s2[i]:
		break

	if s1[i] > s2[i]:
		result = (result + cur) % N
		break

print(result % N)

