from itertools import product as comb
from itertools import permutations as perm
k = int(input())
cubes = [input().split(' ') for i in range(k)]
nums = set()
for n in range(1, k + 1):
    for p in perm(list(range(k)), n):
        for c in comb(list(range(6)), repeat=n):
            nn = ''
            for i in range(n):
                nn += cubes[p[i]][c[i]]
            nums.add(int(nn))
ans = 0
while ans + 1 in nums:
    ans += 1
print(ans)
