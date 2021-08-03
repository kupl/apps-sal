import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    flag = 0
    for i in range(n):
        if a[i] % b[0] != 0:
            if a[i] != b[i]:
                flag = 1
                break
    if flag:
        print("NO")
        continue
    print("YES")
