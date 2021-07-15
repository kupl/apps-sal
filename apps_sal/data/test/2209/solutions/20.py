# n = int(input())
# occurences = [''] * n
# t = [0] * n

# for i in range(n):
#     s = input()
#     occurences[i] = s
#     num_s = s.count('s')
#     num_h = s.count('h')
#     if num_h>0:
#         t[i]=num_s/num_h
#     else:
#         t[i]=10000000

# order = list(range(n))
# order.sort(reverse=True,key=lambda i:t[i])
# dum = ''
# for i in order:
#     dum += occurences[i]

# a = 0
# b = 0
# for c in dum:
#     if c=='s':
#         a+=1
#     else:
#         b+=a
# print(b)
import sys
import functools

def sdiff(a, b):
    nas, nah, nbs, nbh = 0, 0, 0, 0

    for c in a:
        if c == 's':
            nas += 1
        elif c == 'h':
            nah += 1

    for c in b:
        if c == 's':
            nbs += 1
        elif c == 'h':
            nbh += 1

    return nbs * nah - nas * nbh

n = int(sys.stdin.readline().strip())
s = sorted(sys.stdin.readlines(), key=functools.cmp_to_key(sdiff))

r, rs = 0, 0

for ss in s:
    for c in ss:
        if c == 's':
            rs += 1
        elif c == 'h':
            r += rs

print(r)
