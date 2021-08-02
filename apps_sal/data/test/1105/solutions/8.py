import sys
from array import array

f = sys.stdin
n = int(f.readline())
ans = 'YES'
submissions = [0] * n
i = 0
for line in f:
    arr = line.split(" ")
    x = int(arr[0])
    k = int(arr[1]) - 1
    while(k < 0 or k >= len(submissions)):
        submissions.extend([0] * len(submissions))
    if(submissions[k] < x):
        ans = 'NO'
        break
    if(submissions[k] == x):
        submissions[k] = submissions[k] + 1
    i = i + 1
    if(i >= n):
        break
print(ans)
