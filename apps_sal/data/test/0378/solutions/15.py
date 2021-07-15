k, r = [int(x) for x in input().split()]
ans = 0
for i in range(10):
    i = i + 1
    if (i*k)%10 == 0 or (i*k)%10 == r:
        ans = i
        break
print(ans)

