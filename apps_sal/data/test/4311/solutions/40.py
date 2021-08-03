s = int(input())

num_lists = [s]
cnt = 1
while True:
    if (num_lists[-1]) % 2 == 0:
        tmp = num_lists[-1] / 2
    else:
        tmp = (num_lists[-1] * 3) + 1
    cnt += 1
    if tmp in num_lists:
        ans = cnt
        break
    else:
        num_lists.append(tmp)

print(ans)
