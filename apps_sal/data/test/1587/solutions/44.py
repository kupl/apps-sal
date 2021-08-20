N = int(input())
c = str(input())
count_red = 0
flag_red = []
for i in c:
    if i == 'W':
        flag_red.append(0)
    else:
        flag_red.append(1)
        count_red += 1
if count_red == 0:
    ans = 0
else:
    ans = count_red - sum(flag_red[0:count_red])
print(ans)
