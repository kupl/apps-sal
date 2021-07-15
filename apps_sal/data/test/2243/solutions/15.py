def Core(size, rate, data):
	online_rate = []
	count = 0
	for item in data:
		if item[0] == 1:
			if size > count:
				count += 1
				online_rate.append(rate[item[1]])
				online_rate.sort(key=lambda x: -x)
			elif online_rate[-1] < rate[item[1]]:
				online_rate[-1] = rate[item[1]]
				online_rate.sort(key=lambda x: -x)
		else:
			if rate[item[1]] in online_rate and online_rate.index(rate[item[1]]) < size:
				print("YES")
			else:
				print("NO")


param1 = input().split(" ")
param2 = [0] + [int(i) for i in input().split(" ")]
param3 = [[int(j) for j in input().split(" ")] for i in range(int(param1[2]))]
Core(int(param1[1]), param2, param3)
