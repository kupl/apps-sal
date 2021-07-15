def fun(b,d,s):
    if b == d == s:
        return 0
    
    if b > d and b > s:
        return (b-1-d)+(b-1-s)
    if d > b and d > s:
        return (d-1-b)+(d-1-s)
    if s > b and s > d:
        return (s-1-b)+(s-1-d)
    if b == d and b > s:
        return (b-1-s)
    if b == s and b > d:
        return (b-1-d)
    if d == s and d > b:
        return (d-1-b)
    return 0
    
b,d,s = map(int, input().split())
ans = fun(b,d,s)
print(ans)
