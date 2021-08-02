n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))
ans = []
for i in range(n):
    temp = t - h[i] * 0.006
    s = abs(temp - a)
    ans.append(s)
print((ans.index(min(ans)) + 1))
