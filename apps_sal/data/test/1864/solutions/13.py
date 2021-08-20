import time
n = int(input())
A = [int(i) for i in input().split()]
start = time.time()
if 1 in A:
    ans = -1
else:
    ans = 1
print(ans)
finish = time.time()
