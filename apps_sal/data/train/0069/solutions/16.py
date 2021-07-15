import sys,math
# import re
# from heapq import *
# from collections import defaultdict as dd
# from collections import Counter as cc
# sys.setrecursionlimit(10**6)#thsis is must
mod = 10**9+7; md = 998244353
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int,input().split()))
#______________________________________________________
for _ in range(int(input())):
	a,b = inp()
	s = str(input())
	ans = []
	c = 0
	for i in s:
		if i=="1":
			c+=1
		else:
			if c==0:
				continue
			ans.append(c)
			c=0
	if c>0:ans.append(c)
	flag = False
	c =0
	res = []
	for i in s:
		if i=="1":
			flag = True
		if flag==True:
			if i=="0":
				c+=1
			else:
				if c==0:
					continue
				res.append(c)
				c = 0
	# print(res)
	# print(ans)
	fin = 0
	if len(ans)>0:
		fin+=a
	if len(ans)>1:
		for i in range(len(res)):
			if res[i]*b>a:
				fin+=a
			else:
				fin+=res[i]*b
	print(fin)


