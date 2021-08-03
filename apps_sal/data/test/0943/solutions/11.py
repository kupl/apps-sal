n = int(input())
l = list(map(int, input().split()))
s = sorted([x for x in l if x % 2 > 0])
t = sum(l)
if t % 2:
    t -= s[0]
print(t)
