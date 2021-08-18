import string
import sys

n, k = list(map(int, input().split()))

if(k > n or k > 26):
    print(-1)
    return

if(k == 1 and n > 1):
    print(-1)
    return

if(k == 1 and n == 1):
    print('a')
    return

if(k % 2 == 0 and n % 2 == 1):
    rightnum = k - 2
    leftnum = n - rightnum
    leftnum //= 2
    left = 'ab' * leftnum
    left += 'a'
    right = string.ascii_lowercase[2: 2 + rightnum]
    print(left + right)
    return

if(k % 2 == 0 and n % 2 == 0):
    rightnum = k - 2
    leftnum = n - rightnum
    leftnum //= 2
    left = 'ab' * leftnum
    right = string.ascii_lowercase[2:2 + rightnum]
    print(left + right)
    return

if(k % 2 == 1 and n % 2 == 0):
    rightnum = k - 2
    leftnum = n - rightnum
    leftnum //= 2
    left = 'ab' * leftnum
    left += 'a'
    right = string.ascii_lowercase[2: 2 + rightnum]
    print(left + right)
    return

if(k % 2 == 1 and n % 2 == 1):
    rightnum = k - 2
    leftnum = n - rightnum
    leftnum //= 2
    left = 'ab' * leftnum
    right = string.ascii_lowercase[2:2 + rightnum]
    print(left + right)
    return
