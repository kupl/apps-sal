(k, a, b) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(3)]
B = [list(map(int, input().split())) for _ in range(3)]
wina = winb = ca = cb = 0
ls = [(0, 0)]
dic = {}
pre = k
cycle = k
for i in range(k):
    if (a - b + 3) % 3 == 1:
        wina += 1
    elif (a - b + 3) % 3 == 2:
        winb += 1
    ls.append((wina, winb))
    if (a, b) in dic:
        pre = dic[a, b]
        cycle = i - pre
        ca = wina - ls[pre + 1][0]
        cb = winb - ls[pre + 1][1]
        break
    dic[a, b] = i
    (a, b) = (A[a - 1][b - 1], B[a - 1][b - 1])
wina = ls[(k - pre) % cycle + pre][0] + ca * ((k - pre) // cycle)
winb = ls[(k - pre) % cycle + pre][1] + cb * ((k - pre) // cycle)
print('%d %d' % (wina, winb))
