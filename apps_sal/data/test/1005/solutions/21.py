for i in range(int(input())):
    (n, k, d) = map(int, input().split())
    s = list(map(int, input().split()))
    ch = set()
    for i in range(n - d + 1):
        ch.add(len(set(s[i:i + d])))
    print(min(ch))
