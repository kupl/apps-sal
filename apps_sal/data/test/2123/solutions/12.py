#! /usr/bin/env python3

n = int(input())
numbers = [int(x) for x in input().split()]

m = 0

for n in numbers:
	if (n > m):
		m = n

print(m)


