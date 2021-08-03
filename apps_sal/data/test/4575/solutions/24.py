n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
ans = 0
for i in a:
    ans += ((d - 1) // i)
    ans += 1
print(ans + x)
