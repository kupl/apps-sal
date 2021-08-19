ls = [int(i) % 3 for i in input()]
ls.reverse()
cnt = 0
lst = 0
sub = 0
for i in ls:
    if i == 0 or lst + i == 3 or sub + i == 3:
        sub = 0
        lst = 0
        cnt += 1
    else:
        lst = (lst + i) % 3
        sub = i
print(cnt)
