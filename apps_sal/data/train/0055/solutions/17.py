import sys
def input(): return sys.stdin.readline().rstrip()


for _ in range(int(input())):
    n = int(input())
    print(n // 2 + (1 if n % 2 else 0))
