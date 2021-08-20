t = int(input())
for _ in range(t):
    a = int(input())
    ans = 2 ** sum([a >> i & 1 for i in range(32)])
    print(ans)
