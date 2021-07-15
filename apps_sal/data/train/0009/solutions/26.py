import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
input = stdin.readline
#print = stdout.write
letters = ascii_letters[:26]
 
for _ in range(int(input())):
    arr = list(map(int, input().strip()))
    lens = []
    count = 0
    for i in arr:
        if i == 0:
            if count > 0:
                lens.append(count)
            count = 0
        else:
            count += 1
    if count > 0:
        lens.append(count)
    lens.sort(reverse=True)
    res = 0
    for i in range(0, len(lens), 2):
        res += lens[i]
    print(res)

