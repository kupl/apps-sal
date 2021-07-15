
import sys
sys.setrecursionlimit(10000)
# default is 1000 in python


t = int(input())
# t = 1

for _ in range(t):
	b = input()
	a = b[0]
	for i in range(1,len(b)-1,2):
		a += b[i]
	a += b[-1]
	print(a)



# try:
	# raise Exception
# except:
	# print("-1")
	

# thenos.sort(key=lambda x: x[2], reverse=True)

# int(math.log(max(numbers)+1,2))

# 2**3 (power)

# a,t = (list(x) for x in zip(*sorted(zip(a, t))))

# to copy lists use .copy()

# pow(p, si, 1000000007) for modular exponentiation

# my_dict.pop('key', None)
# This will return my_dict[key] if key exists in the dictionary, and None otherwise.




