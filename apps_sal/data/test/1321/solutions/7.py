class Struct:
	pass
	
def algorithm():
	try:	
		sum = 0
		count = int(input())
		max_1 = Struct()
		max_2 = Struct()
		max_1.height = 0
		max_1.id = 0
		max_2.height = 0
		max_2.id = 0
		
		if not (2 <= count <= 200000):
			return None
			
		arr = list()
		for i in range(0, count):
			param = input().split(' ')
			width = int(param[0])
			height = int(param[1])
			if (1 <= width <= 10) and (1 <= height <= 1000):
				if height >= max_1.height:
					max_2.height = max_1.height
					max_2.id = max_1.id
					max_1.height = height
					max_1.id = i
				elif height > max_2.height:
					max_2.height = height
					max_2.id = i
				sum += width
				arr.append(width)
			else:
				return None
		
		result = ''
		for i in range(0, count):
			w = sum - arr[i]
			if i == max_1.id:
				h = max_2.height
			else:
				h = max_1.height
			result += str(w * h)
			if i < count - 1: result += ' '
		print(result)
			
	except BaseException:
		return None
	
algorithm()
