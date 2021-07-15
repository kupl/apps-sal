#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://codeforces.com/contest/1003/problem/D
"""

from typing import List
from collections import defaultdict
from sys import stdin, stdout


def binarySearch(arr: List, low: int, high: int, val: int):
	ans = 0
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] > val:
			high = mid - 1
		elif arr[mid] == val:
			return mid
		else:  #2**mid<val:
			ans = mid
			low = mid + 1
	return ans


N, Q = list(map(int, stdin.readline().split()))
coins = sorted(list(map(int, stdin.readline().split())))

freq = defaultdict(int)
for word in coins:
	freq[word] += 1

coins = sorted(list(freq.keys()))

for _ in range(Q):
	num = int(stdin.readline())
	index = binarySearch(coins, 0, len(coins) - 1, num)
	ans = 0
	while index >= 0 and num > 0:
		used = num // coins[index]
		if used >= freq[coins[index]]:
			used = freq[coins[index]]
		num -= coins[index] * used
		ans += used
		index -= 1
	if num == 0:
		stdout.write(str(ans))
	else:
		stdout.write('-1')
	stdout.write('\n')
"""
/***

5 4
2 4 8 2 4
8
5
14
10
---
1
-1
3
2

5 5
2 4 8 2 1073741824
8
5
14
10
1073741824
---
1
-1
3
2
1

***/
"""
