import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    c = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            c += 1
    print((c + 1) // 2)
