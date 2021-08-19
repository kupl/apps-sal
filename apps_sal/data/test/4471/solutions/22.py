import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = [*map(int, input().split())]
    p = x.pop()
    print('YES' if all(((p - i) % 2 == 0 for i in x)) else 'NO')
