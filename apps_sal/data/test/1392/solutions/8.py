import sys
(n, k) = list(map(int, sys.stdin.readline().split()))
count = 0
while n > 0:
    num = input()
    i = 0
    while i <= k:
        if str(i) not in num:
            break
        i += 1
    if i > k:
        count += 1
    n -= 1
print(count)
