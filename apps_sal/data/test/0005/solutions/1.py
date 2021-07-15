from sys import stdin as cin
from sys import stdout as cout

def main():
    n, pos, l, r = list(map(int, cin.readline().split()))
    if l == 1 and r == n:
        print(0)
        return
    if l == 1:
        print(1 + abs(r - pos))
        return
    if r == n:
        print(1 + abs(pos - l))
        return
    if l == r:
        print(2 + abs(pos - l))
        return
    print(2 + min(abs(r - pos), abs(l - pos)) + r - l)

main()

