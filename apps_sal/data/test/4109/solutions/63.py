n,m,x = list(map(int,input().split()))

array = [list(map(int,input().split())) for _ in range(n)]

# print(array)
# print(n)
ans = 10 ** 8
for i in range(2**n):

    skill = [0] * m
    price = 0
    count = 0
    for k in range(n):
        if (i >> k) & 1:

            price += array[k][0]
            for j in range(m):
                skill[j] += array[k][j+1]
    for l in range(m):
        if skill[l] < x:
            break
        else:
            count += 1
    if count == m:
        ans = min(ans, price)

if ans == 10**8:
    print((-1))
else:
    print(ans)




