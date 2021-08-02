import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    re = False
    for i in range(len(num)):
        for j in range(i + 2, len(num)):
            if num[i] == num[j]:
                re = True
                break
        if re:
            break
    if re:
        print('YES')
    else:
        print('NO')
