def LI():
    return list(map(int, input().split()))


L, R = LI()
ans = 2020
for i in range(L, R+1):
    for j in range(i+1, R+1):
        y = (i*j) % 2019
        ans = min(ans, y)
        if ans == 0:
            break
    if ans == 0:
        break
print(ans)

