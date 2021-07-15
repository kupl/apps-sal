a, b, c, d = map(int, input().split())

obj1 = a*b
obj2 = c*d

if obj1 < obj2:
    ans = obj2
elif obj2 < obj1:
    ans = obj1
else:
    ans = obj1

print(ans)
