s = input().strip()
counter = {'x': 0, 'y': 0}
for ch in s:
	counter[ch] += 1
diff = counter['x'] - counter['y']
if (diff >= 0):
	print("".join(['x'] * diff))
else:
	diff = - diff
	print("".join(['y'] * diff))
		

