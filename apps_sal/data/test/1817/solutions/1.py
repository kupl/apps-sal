def inp():
    return list(map(int, input().split()))
        
n = int(input())
a = sorted(list(inp()))
t = 1
while len(a) != 1:
    if t == 1:
        t = 2
        del a[-1]
    else:
        t = 1
        del a[0]
print(a[0])


