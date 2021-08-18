import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    if n * 2 > m:
        print("YES")
    else:
        print("NO")


for i in range(int(sys.stdin.readline().strip())):
    main()
