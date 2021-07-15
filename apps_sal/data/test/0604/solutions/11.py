#
n = int(input())
from collections import Counter
a = Counter(list(map(int,input().split())))
if 0 in a:
	print (len(a)-1)
else:
	print (len(a))
