import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
m1 = max(list(map(int, input().split())))
n = int(input())
m2 = max(list(map(int, input().split())))
print(m1, m2)
