# n = int(input())
a, b, c, d = list(map(int, input().split()))
t = [a, b, c]
t.sort()
ans = 0
if t[2] - t[1] <= d:
    ans += d - t[2] + t[1]
if t[1] - t[0] <= d:
    ans += d - t[1] + t[0]
print(ans)
# a = [int(i) for i in input().split()]
