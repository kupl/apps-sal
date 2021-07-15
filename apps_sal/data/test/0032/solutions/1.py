#!/usr/bin/env python3

def main():
    n = int(input())
    cur = 0
    for i in range(n):
        x, d = input().split()
        if d == "South":
            cur += int(x)
            if cur > 20000:
                print("NO")
                return
        elif d == "North":
            cur -= int(x)
            if cur < 0:
                print("NO")
                return
        elif cur in (0, 20000):
            print("NO")
            return

    print("YES" if cur == 0 else "NO")

main()

