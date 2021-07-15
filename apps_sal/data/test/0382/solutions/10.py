#list_int 並べて出力 print (' '.join(map(str,ans_li)))
#list_str 並べて出力 print (' '.join(list))

# 2進数 format(10, 'b') # '1010'

''' 二次元配列を一列ずつ
for i in ans:
	print(*i)
'''
''' heapq
queue = []
heapq.heapify(queue) #heapqの作成
heapq.heappush(queue,num) #numのpush(値の追加)
pop = heapq.heappop(queue) #numのpop(最小値の出力)
pop = heapq.heappushpop(queue,num) #push -> pop

'''

from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,M,q = inpl()
S = input()
T = input()
azu = [0]*(N-M+1)
qq = []

for i in range(q):
	qq.append(inpl())

if M > N:
	for i in range(q):
		print(0)
	return

for i in range(0,N-M+1):
	if S[i:i+M] == T:
		azu[i] = 1

SUM = 0
nyan = [0]
for az in azu:
	SUM += az
	nyan.append(SUM)


for l,r in qq:
	l -= 1
	if r - l < M:
		print(0)
	else:
		print(nyan[r-M+1] - nyan[l])

