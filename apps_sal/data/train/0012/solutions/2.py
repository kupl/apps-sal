import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pos = neg = False
    ok = True
    for i in range(n):
        if a[i] > b[i] and not neg:
            ok = False
            break
        if a[i] < b[i] and not pos:
            ok = False
            break
        if a[i] == -1:
            neg = True
        if a[i] == 1:
            pos = True
    print('YES' if ok else 'NO')
