
import time

n = int(input())
a = [int(i) for i in input().split()]

start = time.time()
ans = 0
i = 0

while(i < len(a)):
    if a[i] == 1:
        break
    i += 1


while(i < len(a) - 1):
    if a[i] == 0 and a[i + 1] == 1 and a[i - 1] == 1:
        a[i] = 1
        i
    i += 1

print(sum(a))

finish = time.time()
