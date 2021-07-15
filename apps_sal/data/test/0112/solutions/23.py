from itertools import product as comb
from itertools import permutations as perm
k = int(input())
cubes = [input().split(" ") for i in range(k)]
nums = set()
for n in range(1, k + 1):
    for p in perm(list(range(k)), n):
#        print(p)
        # p is (0, 2, 1) order of cubes
        for c in comb(list(range(6)), repeat=n):
 #           if p == (1, 0):
#                print("--" + str(c))
            nn = ""
            for i in range(n):
  #              if p == (1, 0):
   #                 print("----" + str(p[i]) + "-" + str(c[i]) + "-" + cubes[p[i]][c[i]])
                nn += cubes[p[i]][c[i]]
            nums.add(int(nn))
#print("fuckwrvbwoe")
#print("yes" if 12 in nums else "no")
#print(nums)
ans = 0
while ans + 1 in nums:
    ans += 1
print(ans)

