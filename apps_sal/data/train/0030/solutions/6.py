import sys


def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    res = 0
    i = 0
    while i < n:
        while i < n and s[i] != '1':
            i += 1
        if i >= n:
            break
        while i < n and s[i] == '1':
            i += 1
            res += 1
        i += 1
        res -= 1
    i = 0
    ans = 0
    while i < n:
        while i < n and s[i] != '0':
            i += 1
        if i >= n:
            break
        while i < n and s[i] == '0':
            i += 1
            ans += 1
        i += 1
        ans -= 1
    print(max(ans, res))


for i in range(int(sys.stdin.readline().strip())):
    main()
