import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    alt = 0
    ans = []
    for i in range(len(arr)):
        if k%2==1:
            if arr[i] < k/2:
                ans.append(0)
            else:
                ans.append(1)
        else:
            if arr[i] == k//2:
                ans.append(alt%2)
                alt += 1
            elif arr[i] < k//2:
                ans.append(0)
            else:
                ans.append(1)
                
    print(*ans)
