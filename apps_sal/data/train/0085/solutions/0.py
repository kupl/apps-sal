import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    x = int(input())
    n = len(s)
    ans = ["1" for i in range(n)]
    for i in range(n):
        if s[i] == "0":
            if i - x >= 0:
                ans[i - x] = "0"
            if i + x < n:
                ans[i + x] = "0"
    for i in range(n):
        if s[i] == "1":
            check = False
            if i - x >= 0:
                check |= (ans[i - x] == "1")
            if i + x < n:
                check |= (ans[i + x] == "1")
            if not check:
                print(-1)
                break
    else:
        print("".join(ans))
