import sys

first = sys.stdin.readline().split(" ")
n = int(first[0])
l = int(first[1])
x = int(first[2])
y = int(first[3])
second = sys.stdin.readline().split(" ")

have_dict = {}
need_dict_x = {}
need_dict_y = {}

for val in second:
	have_dict[val] = 1
	val = int(val)
	need_dict_x[str(val - x)] = 1
	need_dict_x[str(val+x)] = 1
	need_dict_y[str(val - y)] = 1
	need_dict_y[str(val + y)] = 1


need_x = 1
need_y = 1
something = 1
for val in have_dict.keys():
	try:
		need_dict_x[val]
		need_x = 0
	except:
		something += 1
	try: 
		need_dict_y[val]
		need_y = 0
	except:
		something -= 1
need_vals = []
if need_x == 1 and need_y == 1:
	to_return = 2
	return_val = str(x) + " "+str(y)
	for val in need_dict_x.keys():
		if int(val) < 0 or int(val) > l: 
			continue
		else:
			try: 
				need_dict_y[val]
				to_return = 1
				return_val = val
			except:
				continue
	print(to_return)
	print(return_val)
else:	
	print(need_x+need_y)
	if need_x == 1:
		print(x)
	elif need_y == 1:
		print(y)
