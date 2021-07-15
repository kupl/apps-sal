def testcase():

    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    while i < n:
        if arr[i] == 1:
            break
        i += 1
    i += 1
    ans = 0
    zs = 0
    while i < n:
        if arr[i] == 0:
            zs += 1
        else:
            ans += zs
            zs = 0
        i += 1
    print(ans)
    return


import sys, os
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
t = int(input())
for _ in range(t):
    testcase()
