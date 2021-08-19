import itertools
dish = [int(input()) for _ in range(5)]
dishp = list(itertools.permutations(dish, 5))
# print(list(dishp))
ans = sum(dish) * 10

for dp in dishp:
    temp = 0
    cnt = 0
    dp = list(dp)
    while len(dp) > 0:
        now = dp.pop(0)
        cnt += 1
        if cnt < 5:
            if now % 10 == 0:
                temp += now
            else:
                temp += (now // 10 + 1) * 10
        else:
            temp += now
            # print(temp,now)
            ans = min(ans, temp)

print(ans)
