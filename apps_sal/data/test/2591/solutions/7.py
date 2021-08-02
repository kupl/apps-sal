import math
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    cur = n // 2
    if n % 2 == 0:
        flag = True
    else:
        flag = False
    for i in range(n):
        if flag == True:
            ans.append(arr[cur])
            cur -= (i + 1)
            flag = False
        else:
            ans.append(arr[cur])
            cur += (i + 1)
            flag = True

    print(*ans)
