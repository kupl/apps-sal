def f(x):
	if x < 10:
		return "0" + str(x)
	return str(x)

n = int(input())
times = []
for i in range(0, n):
	s = input()
	times.append(60 * int(s[0:2]) + int(s[3:5]))
	times.append(60 * 24 + 60 * int(s[0:2]) + int(s[3:5]))
times.sort()
ans = times[1] - times[0] - 1
for i in range(1, len(times)):
	ans = max(ans , times[i] - times[i - 1] - 1) 
print("{}:{}".format(f(ans // 60), f(ans % 60)))
