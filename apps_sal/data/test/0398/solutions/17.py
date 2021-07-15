#!/usr/bin/env python3
def ri():
    return list(map(int, input().split()))

n = int(input())

a = list(ri())

a.sort()

for i in range(len(a)-2):
    if a[i] + a[i+1] > a[i+2]:
        print("YES")
        return

print("NO")

