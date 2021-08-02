n = int(input())
t, a = map(int, input().split())
high = list(map(int, input().split()))
ans = []
for i in range(n):
    m = t - high[i] * 0.006
    b = abs(m - a)
    ans.append(b)

print(ans.index(min(ans)) + 1)
