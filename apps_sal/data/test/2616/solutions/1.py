import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = a.count(1)
    if x == n:
        if n % 2:
            print('First')
        else:
            print('Second')
        continue
    for i in range(n):
        if a[i] == 1:
            continue
        else:
            ind = i
            break
    if ind % 2:
        ans = 2
    else:
        ans = 1
    if ans == 1:
        print('First')
    else:
        print('Second')
