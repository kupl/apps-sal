n = int(input())
str_n = str(n)
keta = len(str_n)
suji = [str(i) for i in range(10)]
ans = 0
for i in range(int(str_n[0]), 10):
    tmp = ''
    for j in range(keta):
        tmp += suji[i]
    if int(tmp) >= n:
        ans = int(tmp)
        break
print(ans)
