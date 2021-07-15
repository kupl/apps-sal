# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = list(map(int,readline().split()))
*a, = list(map(int,readline().split()))
*b, = list(map(int,readline().split()))
b = b[::-1]
from collections import Counter
d = Counter(a+b)
if max(d.values()) > n:
    print("No")
    return

same = set(i for i in range(n) if a[i]==b[i])
from random import randrange
while same:
    i = same.pop()
    while True:
        j = randrange(0,n)
        if a[j] != b[i] and a[i] != b[j]:
            b[i],b[j] = b[j],b[i]
            same.discard(j)
            break

print("Yes")
print((*b))

