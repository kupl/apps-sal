def __starting_point():
	n = int(input())
	arr = input()
	result = -1
	compstr = 'ACTG'
	for i in range(len(arr) - 3):
		substr = arr[i:i+4]
		temp = 0
		for j in range(len(substr)):
			x = abs(ord(compstr[j]) - ord(substr[j]))
			if x > 13:
				x = 26 - x
			temp += x
		if result == -1 or result > temp:
			result = temp
	print(result)
__starting_point()
