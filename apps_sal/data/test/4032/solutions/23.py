(n, k) = list(map(int, input().split()))
lst = list(map(int, input().split()))
cnt = 0
while n and lst[0] <= k:
    lst.pop(0)
    n -= 1
    cnt += 1
while n and lst[n - 1] <= k:
    lst.pop(n - 1)
    n -= 1
    cnt += 1
print(cnt)
