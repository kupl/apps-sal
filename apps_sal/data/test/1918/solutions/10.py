#!/usr/bin/env python3

N = int(input())
arr = list(map(int, input().split()))
teams = input()

initial = sum(arr[i] for i in range(N) if teams[i] == 'B')
best = initial

# prefixes
cur = initial
for i in range(N):
    if teams[i] == 'B':
        cur -= arr[i]
    else:
        cur += arr[i]
        if cur > best:
            best = cur

# suffixes
cur = initial
for i in range(N-1, -1, -1):
    if teams[i] == 'B':
        cur -= arr[i]
    else:
        cur += arr[i]
        if cur > best:
            best = cur

print(best)

