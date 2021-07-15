#!/usr/bin/env python3

import sys

[n, T] = list(map(int, sys.stdin.readline().strip().split()))
ais = list(map(int, sys.stdin.readline().strip().split()))
tis = list(map(int, sys.stdin.readline().strip().split()))

i_0 = [i for i in range(n) if tis[i] == T]
i_hot = [i for i in range(n) if tis[i] > T]
i_cold = [i for i in range(n) if tis[i] < T]

tis = [abs(ti - T) for ti in tis]
w_hot = sum(ais[i] * tis[i] for i in i_hot)
w_cold = sum(ais[i] * tis[i] for i in i_cold)

if w_hot > w_cold:
	w_hot, w_cold = w_cold, w_hot
	i_hot, i_cold = i_cold, i_hot

x_max = sum(ais[i] for i in i_0) + sum(ais[i] for i in i_hot)

w = w_hot
i_cold.sort(key=lambda _k: tis[_k])
for i in i_cold:
	a, t = ais[i], tis[i]
	if a * t <= w:
		w -= a * t
		x_max += a
	else:
		x_max = x_max + float(w) / t
		w = 0
		break


print(float(x_max))

