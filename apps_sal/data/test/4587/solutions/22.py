#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

a_index = 0
b_index = 0
c_index = 0

bc = []
while(b_index < len(b) and c_index < len(c)):
    if b[b_index] < c[c_index]:
        bc.append(len(c) - c_index)
        b_index += 1
    else:
        c_index += 1
    # print(b_index, c_index)

if len(bc) == 0:
    print((0))
    return

bc_sum = [bc[-1]]
for i in reversed(bc[:-1]):
    bc_sum.append(i + bc_sum[-1])
bc_sum = list(reversed(bc_sum))

# print(bc)
# print(bc_sum)
a_index = 0
b_index = 0
c_index = 0
ans = []
while(a_index < len(a) and b_index < len(b) and b_index < len(bc_sum)):
    if a[a_index] < b[b_index]:
        # ans.append(sum(bc[b_index:]))
        ans.append(bc_sum[b_index])
        a_index += 1
    else:
        b_index += 1
    # print(a_index, b_index)

# print(bc)
print((sum(ans)))
