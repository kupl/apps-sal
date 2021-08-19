import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n and a == sorted(a)[::-1]:
        print('NO')
    else:
        print('YES')
