import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = input()
    n = len(s)
    ls = []
    if s[0] == ".":
        cnt = 1
    else:
        cnt = 0
    for i in range(1, n + 1):
        if i < n and s[i] == ".":
            cnt += 1
        else:
            if cnt >= b:
                ls.append(cnt)
            cnt = 0
    if not ls:
        print("NO")
        continue
    ls.sort()
    if a >= 2 * b:
        if len(ls) >= 2 or ls[0] > a + (b - 1) * 2 or ls[0] < a:
            print("NO")
        else:
            print("YES")
    else:
        if ls[0] < a:
            print("NO")
        elif len(ls) >= 2 and ls[-2] >= 2 * b:
            print("NO")
        else:
            l = len(ls) - 1
            t = ls[-1]
            for i in range(t):
                if i + a <= t:
                    p, q = i, t - (i + a)
                    if not (b <= p < a or b <= q < a or p >= 2 * b or q >= 2 * b):
                        x = l + (a <= p < 2 * b) + (a <= q < 2 * b)
                        if x % 2 == 0:
                            print("YES")
                            break
            else:
                print("NO")
