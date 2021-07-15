n = int(input())
a = list(map(int, input().split()))

answer = 0
negative = 0
for i in range(n):
	answer += abs(abs(a[i]) - 1)
	if a[i] < 0:
		negative += 1

if negative % 2 == 1:
	if 0 not in a:
		answer += 2

print(answer)

