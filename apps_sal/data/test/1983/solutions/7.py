import math
from sys import stdin
input = stdin.readline
for i in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = n
    for j in range(n - 1):
        if arr[j + 1] == arr[j]:
            ans -= 1
    print(ans)
