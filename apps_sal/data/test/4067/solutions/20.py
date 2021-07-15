n = int(input())
s = input()

nrml = n // 3
elm_array = [nrml - s.count(str(i)) for i in range(3)]

for i in [0,2,1]: # i = 1
	if elm_array[i] > 0:
		for j in range(3): # j = 0
			if elm_array[j] < 0:
				to_replace = min(elm_array[i], -elm_array[j])
				elm_array[i] -= to_replace
				elm_array[j] += to_replace
				if i > j:
					s = s[::-1].replace(str(j), str(i), to_replace)[::-1]
				else:
					s = s.replace(str(j), str(i), to_replace)

print(s)
