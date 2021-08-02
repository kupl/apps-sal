import math
import sys


def mp():
    return list(map(int, input().split()))


def main():
    n = int(input())
    a = input().strip()
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            print('YES')
            print(a[i] + a[i + 1])
            return
    print("NO")


deb = 0
if deb:
    file = open("input.txt", "r")
    input = file.readline
else:
    input = sys.stdin.readline

main()

if deb:
    file.close()
