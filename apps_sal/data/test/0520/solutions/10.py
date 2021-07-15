#! usr/bin/env python3
year = 0
x = input()
groups = input().split(" ")

for i in range(len(groups)):
	groups[i] = int(groups[i])
	year += groups[i]

year = int(year / len(groups))
print(year)
