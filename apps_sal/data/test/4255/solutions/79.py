a, b, c = map(int, input().split())

ma = max(a, b, c)
if(a == ma):
    ans = b * c
elif(b == ma):
    ans = a * c
else:
    ans = a * b

print(ans // 2)
