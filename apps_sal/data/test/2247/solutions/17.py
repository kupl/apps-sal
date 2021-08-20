t = int(input())
for i in range(t):
    (s, a, b, c) = map(int, input().split())
    q = s // c
    ans = q // a * (a + b) + q % a
    print(ans)
