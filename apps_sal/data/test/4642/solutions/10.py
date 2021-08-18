from collections import defaultdict as dd
import sys
input = sys.stdin.readline
t = int(input())
while t:
    n, x, y = list(map(int, input().split()))
    dif = y - x
    for i in range(n - 1, -1, -1):
        if(dif % i == 0):
            ind = i
            break
    diff = dif // ind
    arr = [x]
    cou = 1
    curr = x
    while curr != y:
        curr += diff
        arr.append(curr)
        cou += 1
    left = n - cou
    curr = x
    while left and curr - diff > 0:
        curr -= diff
        arr.append(curr)
        left -= 1
    curr = y
    while left:
        curr += diff
        arr.append(curr)
        left -= 1
    print(*arr)
    t -= 1
