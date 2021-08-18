n = int(input())
x = input()
x = [i for i in x.split()]
length = {}
for i in x:
    if len(i) not in length:
        length[len(i)] = 1
    else:
        length[len(i)] = length[len(i)] + 1

dict = {}
ans = 0

for i in range(n):
    l = ""
    r = ""
    for j in range(1, 11):
        num = x[i]
        extra = ""
        if len(num) > j:
            extra = num[0:len(num) - j]
        if len(num) - j >= 0:
            l = "0" + num[len(num) - j] + l
            r = num[len(num) - j] + "0" + r
        le = extra + l
        re = extra + r
        if j in length:
            ans += int(le) * length[j]
            ans += int(re) * length[j]
print(ans % 998244353)
