from collections import defaultdict, deque, Counter, OrderedDict
from bisect import insort, bisect_right, bisect_left
import threading, sys

def main():
    n = int(input())
    check = False
    for i in range(n):
        a,b,c = input().split()
        b,c = int(b),int(c)
        if b >= 2400 and c > b:
            check = True
    print("YES" if check else "NO")

def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)"""
    thread = threading.Thread(target=main)
    thread.start()
__starting_point()
