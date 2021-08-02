i = 0
t, sx, sy, ex, ey = list(map(int, input().split()))
second_string = input()
while (sy != ey) or (sx != ex):
    if i == t: break
    if second_string[i] == 'E':
        if sx < ex: sx += 1
    elif second_string[i] == 'W':
        if sx > ex: sx -= 1
    elif second_string[i] == 'N':
        if sy < ey: sy += 1
    elif second_string[i] == 'S':
        if sy > ey: sy -= 1
    i += 1
if (sy == ey and sx == ex) is False: print(-1)
else: print(i)
