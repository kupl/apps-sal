n = int(input())
for i in range(n):
    (a, b) = map(int, input().split())
    ans = (b // a + 1) ** 2 * (b % a) + (b // a) ** 2 * (a - b % a)
    print(ans)
