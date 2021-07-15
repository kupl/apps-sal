x = input("").split(' ')
a = int(x[0])
b = int(x[1])
pow2 = []
for g in range (66):
 pow2.append(1<<g)
def solve (c):
 cnt = 0
 for g in range (66):
   k = 0
   for y in range (g):
    k|=(1<<y)
   for y in range (g+1, 66):
    k|=(1<<y)
    if (k <= c):
     cnt+=1
 return cnt

print(solve(b) - solve(a-1))
