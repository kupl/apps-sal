import sys
input = sys.stdin.readline
al = [list(map(int, input().split())) for _ in range(int(input()))]
al = sorted(al, key=lambda x: x[1])
s = 0
for (i, j) in al:
    s += i
    if s > j:
        print('No')
        break
else:
    print('Yes')
