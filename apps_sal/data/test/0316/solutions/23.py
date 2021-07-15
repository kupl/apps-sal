a= int(input())
ans = 1
k = 4
for i in range(a - 1):
    ans += k
    k += 4
if a == 0:
    print(0)
else:
    print(ans)
