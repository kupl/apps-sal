import sys
from collections import defaultdict
n = int(input())
#n,k = [int(__) for __ in raw_input().split()]
arr = [int(__) for __ in input().split()]
sactive = set()
sactive.add(0)
nums = [0] * n
d1 = defaultdict(set)
d2 = defaultdict(set)
d = defaultdict(set)
lines = sys.stdin.readlines()
for i in range(n-1):
    sactive.add(i+1)
    s,f = [int(__) for __ in lines[i].strip().split()]
    s -= 1
    f -= 1
    d[s].add(f)
    d[f].add(s)
    nums[f] += 1
    nums[s] += 1

leaves = set()



for i in range(n):
    if nums[i] == 1:
        leaves.add(i)
while len(leaves):
    x = leaves.pop()
    if arr[x] == 0:
        sactive.remove(x)
        nums[x] -= 1
        targ = d[x].pop()
        nums[targ] -= 1
        d[targ].remove(x)
        if nums[targ] == 1:
            leaves.add(targ)

sactive1 = sactive.copy()
for targ in d:
    d1[targ] = d[targ].copy()
nums1 = nums[:]
nums2 = nums[:]

for i in range(n):
    if nums1[i] == 1:
        leaves.add(i)
while len(leaves):
    x = leaves.pop()
    if arr[x] != 1:
        sactive1.remove(x)
        nums1[x] -= 1
        targ = d1[x].pop()
        nums1[targ] -= 1
        d1[targ].remove(x)
        if nums1[targ] == 1:
            leaves.add(targ)
            
sactive2 = sactive.copy()
for targ in d:
    d2[targ] = d[targ].copy()

for i in range(n):
    if nums2[i] == 1:
        leaves.add(i)
while len(leaves):
    x = leaves.pop()
    if arr[x] != 2:
        sactive2.remove(x)
        nums2[x] -= 1
        targ = d2[x].pop()
        nums2[targ] -= 1
        d2[targ].remove(x)
        if nums2[targ] == 1:
            leaves.add(targ)

           
if len(sactive1 & sactive2) > 0:
    print(0)
else:
    print(len(sactive) - len(sactive1) - len(sactive2) + 1)
#print(nums)
#print('both',sactive)
#print('1',sactive1)
#print('2',sactive2)
#print(d)

