n = int(input())
(d, x) = map(int, input().split())
a_l = [int(input()) for _ in range(n)]
ans = 0
for a in a_l:
    ans += (d - 1) // a + 1
print(ans + x)
