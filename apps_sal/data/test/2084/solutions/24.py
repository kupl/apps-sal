#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
secondLine = [int(x) for x in input().split()]

print(sum(sorted(secondLine)[:firstLine[1]]))
