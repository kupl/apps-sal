for _ in range (int(input())):
    n, a, b = list(map(int, input().split()))
    ans = ''
    x = []
    for i in range(97, 97 + b):
        x.append(chr(i))
    for i in range(n):
        ans += x[i % b]
    print(ans)
