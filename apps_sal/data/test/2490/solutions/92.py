S = input()
ans = 0
flag = False  # 繰り上がりありならTrue
flag2 = False  # 前が5ならTrue
for k in range(len(S)):
    n = int(S[-k - 1])
    if flag2:
        if n < 5:
            flag = False
        else:
            flag = True
    if flag:
        n += 1
    if n == 5:
        ans += 5
        flag2 = True
        flag = False
    elif n < 5:
        ans += n
        flag2 = False
        flag = False
    else:
        ans += 10 - n
        flag2 = False
        flag = True
if flag:
    ans += 1
print(ans)
