import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(2)
        print(*a)
        continue
    ans = [a[0]]
    if a[1] > a[0]:
        turn = 1
    else:
        turn = 0
    s = abs(a[1] - a[0])
    for i in range(2, n):
        if turn:
            if a[i] > a[i - 1]:
                continue
            ans.append(a[i - 1])
            turn = 0
        else:
            if a[i] < a[i - 1]:
                continue
            ans.append(a[i - 1])
            turn = 1
    ans.append(a[-1])
    print(len(ans))
    print(*ans)
