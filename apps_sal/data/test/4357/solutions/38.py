a,b,c = input().split()

if a == max(a,b,c):
    ans = int(a+b) + int(c)
elif b == max(a,b,c):
    ans = int(b+a) + int(c)
else:
    ans = int(c+a) + int(b)
print(ans)
