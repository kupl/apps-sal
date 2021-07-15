#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-12-03 16:10:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
# print('now')
maxn = 1000010
pre, next, ans, vis = [], [], [], []
for i in range(maxn):
	pre.append(-1)
	next.append(-1)
	ans.append(-1)
	vis.append(0)
n = int(input())
for i in range(n):
	a, b = 	input().split()
	# print('in', a, b)
	x, y = int(a), int(b)
	vis[x] = vis[y] = 1
	pre[y] = x
	next[x] = y
# print('next[2]')
ans[0] = 0
vis[0] = 2
i = 0
j = 2
while next[i] != -1:
	i = next[i]
	if vis[i] == 2:
		break
	ans[j] = i
	j += 2
	vis[i] = 2
j = -1
for i in range(maxn):
	if vis[i] == 1:
		j = i
		break
while pre[j] != -1:
	j = pre[j]
i = j
j = 3
vis[i] = 2
ans[1] = i 
while next[i] != -1:
	i = next[i]
	ans[j] = i
	j += 2
	vis[i] = 2
# print("here")
for i in range(n+2):
	if ans[i] > 0:
		print(ans[i], end = ' ')

