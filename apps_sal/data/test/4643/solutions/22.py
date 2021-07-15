import time
li = list(map(int, input().split()))
n = li.pop(0)
li.sort()
for i in range(20000000):
    s = 0
print(" ".join(map(str, li)))
