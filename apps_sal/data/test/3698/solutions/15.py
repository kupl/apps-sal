# -*- encoding:utf-8 -*-

import sys
from functools import reduce

#sys.stdin = open('C.in', 'r')
def debug(*args):
    return
    print('debug ',end='')
    for x in args:
        print(x,end=' ')
    print('')

n = input()
k = int(input())
mod = 1000000007
#n = '1'*1000
#k = 5

a = [0] * 1001

def bitnum(x):
    ans = 0
    while x:
        if x & 1: ans += 1
        x >>= 1
    return ans

for i in range(1,1001):
    bn = bitnum(i)
    a[i] = a[bn] + 1

#debug([i for i in range(10)])
#debug(a[:10])

''' number of bits that needs k operations to reduce to 1 '''
a = [i for i in range(len(a)) if a[i]==k]
a = list(filter(lambda x: x <= len(n), a))
#debug(a[:10])

C = [None for i in range(1001)]
C[0] = [1, 0]
for i in range(1, len(C)):
    C[i] = [1] + [(C[i-1][j]+C[i-1][j-1])%mod for j in range(1,i)] + [1]

answer = 0

def cal2(x, arr):
    nonlocal answer
    while True:
        ln = len(arr)
        if x == 0:
            answer += 1
            return
        if x > ln: return
        if x == ln:
            if '0' in arr:return
            else:
                answer += 1
                return
        answer += C[ln-1][x]
        answer %= mod
        #debug(ans, x)
        i = arr.find('1', arr.index('1')+1)
        if i < 0: 
            if x == 1: answer += 1
            return
        #debug("***")
        x -= 1
        arr = arr[i:]
        #cal2(x-1, arr[i:])

def cal(x):
    nonlocal answer
    answer = 0
    cal2(x, n)
    debug(answer)
    return answer % mod

def solve():
    if k == 0:return 1
    if len(a) == 0:return 0
    tmp = map(cal,a)
    debug(list(tmp))
    ans = reduce(lambda x,y:(x+y)%mod, map(cal, a))
    return ans if k != 1 else ans-1

try:
    print(solve())
except Exception as e:
    print(k, n[-30:])

#print(solve())

