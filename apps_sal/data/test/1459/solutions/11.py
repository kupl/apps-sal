n = int(input())
a = list(map(int, input().split()))
s, t = list(map(int, input().split()))
s -= 1
t -= 1
if s > t:
    s, t = t, s
x = sum(a[s:t])
y = sum(a[0:s]) + sum(a[t:n])
print(min(x, y))
