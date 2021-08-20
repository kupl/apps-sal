x = int(input())
a = list(map(int, input().split()))
o = a.count(1)
t = a.count(2)
ans = min(o, t)
if o > t:
    o = o - ans
    new = o // 3
    ans = ans + new
print(ans)
