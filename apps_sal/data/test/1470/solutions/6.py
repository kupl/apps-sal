x = int(input())
rem = x%11
cnt = (x-rem)//11
cnt *= 2

if 0 < rem <= 6:
    cnt += 1
elif rem > 6:
    cnt += 2

print(cnt)
