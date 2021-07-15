n, m = list(map(int, input().split()))

foods = []
for i in range(n):
    foods.append(list(map(int, input().split())))

if len(foods) == 1:
    print((len(foods[0])-1))
else:
    ans = 0
    for i in foods[0][1:len(foods[0])]:
        cnt = 0
        for j in range(1, len(foods)):
            if i in foods[j][1:len(foods[j])]:
                cnt += 1
                if cnt == len(foods) - 1:
                    ans += 1

    print(ans)

