a,b = map(int,input().split())
ans = 0
if b-a<=10:
    for i in range(a,b+1):
        ans ^= i
else:
    while a % 4 != 0:
        ans ^= a
        a += 1
    while b % 4 != 3:
        ans ^= b
        b-= 1
print(ans)
