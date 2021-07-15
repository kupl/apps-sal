n = int(input())
a = list(map(int, input().split()))
x = s = 0
for ai in reversed(a):
    x = max(x, ai + s - x)
    s += ai

print(s - x, x)

