# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

A = [*list(map(int, readline().split()))]
A.sort()
a, b, c = A
v = c
ans = 0
while a < v - 1:
    a += 2
    ans += 1
while b < v - 1:
    b += 2
    ans += 1

if a == b == c - 1:
    a += 1
    b += 1
    ans += 1

if a == c - 1:
    ans += 2
if b == c - 1:
    ans += 2

print(ans)
