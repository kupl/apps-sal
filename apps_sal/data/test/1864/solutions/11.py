__author__ = 'tka4a'
n = int(input())
kupurs = list(map(int, input().split()))
kupurs.sort()
if kupurs[0] == 1:
    print(-1)
else:
    print(1)
