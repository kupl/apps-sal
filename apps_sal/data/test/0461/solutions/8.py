n = int(input())
a = int(input())
b = int(input())
c = int(input())
ans = 0
t = 0
n-=1
if n == 0:
    print(0)
    return
if c < a and c < b:
    ans = min(a, b) + (n-1)*c
else:
    ans = min(a, b)*(n)
print(ans)
