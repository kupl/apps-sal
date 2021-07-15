n, m= map(int, input().split())
ps = [list(map(str,input().split())) for _ in range(m)]

str_l = ["WA"]*n
int_l = [0]*n
num = 0
ac = 0

for pp, s in ps:
    p = int(pp)-1
    if s == "AC":
        str_l[p] = "AC"
    else:
        if str_l[p] != "AC":
            int_l[p] += 1

for i in range(n):
    if str_l[i] == "AC":
        num += int_l[i]
        ac += 1

print(ac,num)
