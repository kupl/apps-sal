a, b, c, d, e, f = map(int, input().split())

ans = -1
ans_water = -1
ans_sugar = -1
for ia in range(f//(a*100)+2):
    water = 100*a*ia
    if water > f or water == 0: continue
    for ib in range(f//(b*100)+2):
        if ib != 0: water += 100*b
        if water > f or water == 0: continue
        for ic in range(f//c+1):
            sugar = c*ic
            if sugar/(water//100) > e: continue
            for id in range(f//d+1):
                if id != 0: sugar+=d
                if sugar/(water//100) > e: continue
                if sugar + water > f: continue
                if (100*sugar)/(sugar+water) > ans:
                    ans = (100*sugar)/(sugar+water)
                    ans_water = water
                    ans_sugar = sugar
print(ans_sugar+ans_water, ans_sugar)
