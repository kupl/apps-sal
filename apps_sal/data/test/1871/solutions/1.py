n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
for i in a:
    s+=x*i
    x = max(x-1,1)
print(s)
