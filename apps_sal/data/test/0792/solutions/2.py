n, d = [int(x) for x in input().split()]
tr = [int(x) for x in input().split()]
cash = 0
flag = False
gr = []
for i in tr:
    if i != 0:
        cash += i
    gr.append(cash)
    if cash > d:
        flag = True
        break
if flag:
    print(-1)
else:
    mx = [-1] * n
    mx[-1] = gr[-1]
    for i in range(n - 2, -1, -1):
        mx[i] = max(gr[i], mx[i + 1])
    acash = 0
    count = 0
    for i in range(n):
        if tr[i] == 0:
            if gr[i] + acash < 0:
                acash += (d - mx[i] - acash)
                if gr[i] + acash < 0:
                    count = -1
                    break
                count += 1
    print(count)
