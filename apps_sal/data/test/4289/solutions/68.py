n = int(input())
t, a = list(map(int, input().split()))
l = list(map(int, input().split()))

x = t - l[0] * 0.006
ans = []
for x in l:
    x = t - x * 0.006
    y = a - x
    ans.append(abs(y))

print((ans.index(min(ans)) + 1))
