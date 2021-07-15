n = int(input())
v = list(map(int, input().split()))
for i in range(n-1):
    a = min(v)
    v.remove(a)
    b = min(v)
    v.remove(b)
    new = (a+b)/2
    v.append(new)
print(new)
