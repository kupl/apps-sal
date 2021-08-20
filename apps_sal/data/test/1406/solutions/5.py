import fileinput
import math
for line in fileinput.input():
    inp = [int(i) for i in line.split()]
n = inp[0]
k = inp[1]
d = inp[2]
if n > k ** d:
    print(-1)
else:
    for i in range(d):
        pr = k ** i
        results = [j // pr % k + 1 for j in range(n)]
        print(' '.join(map(str, results)))
