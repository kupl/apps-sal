# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#n,*a = map(int,readline().split())

"""
a = "dream"[::-1]
b = "dreamer"[::-1]
c = "erase"[::-1]
d = "eraser"[::-1]
"""
s = [*input()]
a = [*"dream"]
b = [*"dreamer"]
c = [*"erase"]
d = [*"eraser"]

while True:
    if not s:
        print("YES")
        break
    elif s[-5:] == a:
        for _ in range(5): s.pop()
    elif s[-5:] == c:
        for _ in range(5): s.pop()
    elif s[-7:] == b:
        for _ in range(7): s.pop()
    elif s[-6:] == d:
        for _ in range(6): s.pop()
    else:
        print("NO")
        break





