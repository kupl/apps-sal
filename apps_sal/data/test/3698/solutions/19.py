import sys
import math
from collections import defaultdict, deque
import heapq
fact = [1]
mod = 10**9 + 7
for i in range(1, 1005):
    fact.append((i * fact[-1]) % mod)
# print(fact,'fact')


def comb(n, k, fact):
    # print(n,'n',k,'k')
    x = fact[n]
    y = pow(fact[k], mod - 2, mod)
    z = pow(fact[n - k], mod - 2, mod)
    # print(x,'x',y,'y',z,'z')

    return (x * (y * z)) % mod


def getset(num):
    cnt = 0
    while num > 0:
        cnt += num % 2
        num = num >> 1
    return cnt


def get(s, bits):
    # print(s,'s',bits,'bits')
    n = len(s)
    # print(n,'n')
    if n != 0 and bits == 0:
        return 1
    if n == 0 and bits == 0:
        return 1
    if n == 0:
        return 0
    if s[0] == '1':
        ans = 0
        if n - 1 >= bits:
            ans += comb(n - 1, bits, fact)
            # print(comb(n-1,bits,fact),'comb')
        x = get(s[1:], bits - 1)
        # print(x,'x',s,'s',bits-1,'bitts')
        ans += x
        ans %= mod
        # print(s,'s',ans,bits)
        return ans
    x = get(s[1:], bits)
    x %= mod
    # print(s,'s',x,bits)
    return x


# t=int(sys.stdin.readline())
num = sys.stdin.readline()[:-1]
m = len(num)
n = 0
# print(m,'m')
for i in range(m):
    if num[i] == '1':
        n = (n << 1) + 1
    else:
        n = n << 1
# print(n,'nnnn')
k = int(sys.stdin.readline()[:-1])
if k == 0:
    print(1)
    return
dic = defaultdict(list)
for i in range(2, 1001):
    x = getset(i)
    cnt = 0
    while x != 1:
        y = getset(x)
        cnt += 1
        x = y
    dic[cnt + 1].append(i)
# print(dic,'dic')
ans = 0
'''for i in dic[k]:
    if i<=n:
        ans+=1'''
# ans+=len(dic[k])
# print(n,'n')
# print(num,'num')
s = num
# print(s,'s')
# print(len(s))
dic[0] = [1]
# print(dic[k-1])
for j in dic[k - 1]:
    if j <= n:
        # print(s,'s')
        x = get(s, j)
        # print(x,'xxxxxxxx')
        # print(j,'j')
        # print(x,'x',j,'j',k-1,'k-1')
        ans += x
        # print(x,'x',k-1,'j',j,'j')
        ans %= mod
# ans=get(s,k-1)
if s == '1' and k == 1:
    print(0)
    return
if k == 1:
    ans -= 1
print(ans)
