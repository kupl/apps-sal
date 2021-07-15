w = open('output.txt', 'w')
r = open('input.txt', 'r')
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_date(m, d):
    res = 0
    for i in range(m-1):
        res += arr[i]
    return res + d

n = int(r.readline())
used = [0] * 366
for i in range(n):
    m, d, p, t = list(map(int, r.readline().split()))
    date = get_date(m, d)
    for i in range(max(0, date-t), date):
        used[i] += p
w.write(str(max(used)))

