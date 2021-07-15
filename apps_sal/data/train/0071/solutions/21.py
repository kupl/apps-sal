import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    need = sum([i for i in arr if i >= 0])
    was = 0
    have = [0] * n
    for i in range(n):
        if i != 0:
            have[i] = have[i - 1]
        if arr[i] > 0:
            have[i] += arr[i]
    for i in range(n - 1, -1, -1):
        if arr[i] < 0:
            bf = min(abs(arr[i]), have[i] - was)
            was += bf
            need -= bf
        else:
            was = max(0, was - arr[i])
    print(need)


