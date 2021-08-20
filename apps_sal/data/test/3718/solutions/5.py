import time
n = int(input())
a = [int(i) for i in input().split()]
start = time.time()
a = sorted(list(set(a)))
ans = 'NO'
for i in range(len(a) - 2):
    if a[i + 2] - a[i] <= 2:
        ans = 'YES'
        break
print(ans)
finish = time.time()
