import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        a.sort()
        same = True
        for i in range(n // 2):
            if a[i * 2] != a[i * 2 + 1]:
                same = False
                break
        if same:
            print('Second')
        else:
            print('First')
    else:
        print('Second')
