import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (n, x) = list(map(int, input().split()))
    s = input()
    pre = [1]
    if s[0] == '1':
        pre[0] = -1
    for i in range(1, 2 * n):
        pre.append(pre[i - 1] + 1)
        if i >= n:
            i -= n
        if s[i] == '1':
            pre[-1] -= 2
    if pre[:n] == pre[n:]:
        if x in pre:
            print(-1)
        else:
            print(0)
    else:
        tot = 0
        if x == 0:
            tot += 1
        for i in range(n):
            if (x - pre[i]) % (pre[i + n] - pre[i]) == 0:
                if pre[i] < pre[i + n] and x < pre[i]:
                    continue
                if pre[i] > pre[i + n] and x > pre[i]:
                    continue
                tot += 1
        print(tot)
