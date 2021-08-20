import sys
(n, k) = map(int, sys.stdin.readline().split())
if k == 1 and n != 1 or k > n:
    print(-1)
elif n == 1:
    print('a')
else:
    tmp = n - k + 2
    s = 'ab' * (tmp // 2)
    if tmp % 2 == 1:
        s += 'a'
    for i in range(2, k):
        s += chr(ord('a') + i)
    print(s)
