def LI():
    return list(map(int, input().split()))


a, b, x, y = LI()
ans = abs(a-b)*y+x
if a > b:
    ans -= y
if a == b or a == b+1:
    rouka = x
elif a < b:
    rouka = x
    rouka += (b-a)*x*2
else:
    a -= 1
    rouka = x
    rouka += (a-b)*x*2
ans = min(ans, rouka)
print(ans)

