from sys import stdin, stdout
tests = int(stdin.readline().strip())
for t in range(tests):
    n, m = list(map(int, stdin.readline().strip().split()))
    s = list((list(map(int, stdin.readline().strip().split()))))
    s = s[::-1]
    cur = n
    ans = 0
    while(cur > 0) and len(s) != 0:
        if(cur <= 2):
            break
        while len(s) > 0 and s[-1] >= cur:
            s.pop()
        if(len(s) == 0):
            break
        if cur - s[-1] > 1:
            cur = s[-1] + 1
            continue
        if len(s) == 1:
            ans += 1
            break
        if (s[-2] + 1) == s[-1]:
            cur = s[-2]
            continue
        ans += 1
        cur = s[-2] + 1
    print(ans)
