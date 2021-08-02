import io
import sys
import time
import random
# ~ start = time.clock()
# ~ test = '''2 2 1 1
# ~ 1 2'''
# ~ test = '''3 2 3 3
# ~ 1 1
# ~ 3 1
# ~ 2 2'''
# ~ test = '''3 2 3 2
# ~ 1 1
# ~ 3 1
# ~ 2 2'''

# ~ sys.stdin = io.StringIO(test)

r, c, n, k = list(map(int, input().split()))  # row column number-of-violists
data = [[0 for i in range(c)] for j in range(r)]
#~ print(r,c,n,k)

for i in range(n):
    x, y = list(map(int, input().split()))  # row column
    data[x - 1][y - 1] = 1

nviolists = [[0 for i in range(c)] for j in range(r)]

for r1 in range(r):
    count = 0
    for c1 in range(c):
        count += data[r1][c1]
        nviolists[r1][c1] = (nviolists[r1 - 1][c1] if r1 > 0 else 0) \
            + count
        #~ print(r1,c1,nviolists[r1][c1],nviolists[r1][c1-1])
        #~ print(nviolists)

count = 0
for r1 in range(r):
    for r2 in range(r1, r):
        for c1 in range(c):
            for c2 in range(c1, c):
                # between (r1,c1) and (r2,c2)

                vcount = nviolists[r2][c2] \
                    - (nviolists[r1 - 1][c2] if r1 > 0 else 0) \
                    - (nviolists[r2][c1 - 1] if c1 > 0 else 0) \
                    + (nviolists[r1 - 1][c1 - 1] if r1 * c1 > 0 else 0)
                if vcount >= k:
                    #~ print( (r1,c1), (r2,c2) )
                    count += 1


print(count)
# ~ dur = time.clock()-start
#~ print("Time:",dur)
