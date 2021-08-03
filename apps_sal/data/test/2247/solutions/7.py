t = int(input())
for i in range(t):
    s, a, b, c = map(int, input().split())
    x = s // (a * c)
    ans = x * (a + b)
    s -= x * a * c
    ans += s // c
    print(ans)
