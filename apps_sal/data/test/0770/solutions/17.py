n = int(input())

x = list(map(int,input().split()))

current_state = 0
answer = 0

for i in range(n):
	if x[i] == 0 and current_state == 0:
		continue

	if x[i] == 0:
		current_state = 0
		answer += 1

	if x[i] != 0:
		answer += 1
		current_state = 1

if x[n-1] == 0 and answer != 0:
	answer -=1

print(answer)
