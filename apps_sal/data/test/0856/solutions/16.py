input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    for _ in range((k + 1) % 2 + 1):
        f = max(s)
        for i in range(n):
            s[i] = f - s[i]
    print(*s)
