data = input().split("+")
data = [int(x) for x in data]
ones = 0
twos = 0
threes = 0
for number in data:
	if number == 1:
		ones += 1
	elif number == 2:
		twos += 1
	elif number == 3:
		threes += 1
ans = ""
for i in range(ones):
	ans += '1'
	ans += '+'
for i in range(twos):
	ans += '2'
	ans += '+'
for i in range(threes):
	ans += '3'
	ans += '+'
ans = ans[:-1]
print(ans)
