def mi():
	return list(map(int, input().split()))
'''
3
aa
abacaba
xdd
'''
from collections import Counter as c
for _ in range(int(input())):
	li = list(input())
	s = c(li)
	if len(s)==1:
		print(-1)
	else:
		print(''.join(sorted(li)))

