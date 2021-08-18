import sys
input = sys.stdin.readline
def ri(): return int(input())
def rl(): return list(map(int, input().split()))
def rs(): return input().strip("\r\n")


for _ in range(1):
    n = ri()
    t = rs()
    copies = 1e10
    ans = 0
    s = '110' * (n)
    for i in range(3):
        if t != s[i:i + n]:
            continue
        ans += copies - (i + n - 1) // 3
    print(int(ans))
