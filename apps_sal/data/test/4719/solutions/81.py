from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n = readInt()
sn = [list(input()) for i in range(n)]
snc = [Counter(sn[i]) for i in range(n)]

s = set(sn[0])
for i in range(n):
	s = s & set(sn[i])

s = sorted(list(s))
ans = ""
for c in s:
	m = float("inf")
	for i in range(n):
		m = min(m, snc[i][c])
	ans+=c*m

print(ans)
