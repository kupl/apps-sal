s = input()
n, m = list(map(int, s.split()))
port = []
for i in range(n):
    ss = input()
    p = list(map(int, ss.split()))
    port.append(p)
mar = 0
for each in port:
    if each[0] > mar:
        print('NO')
        return
    else:
        if each[1] > mar:
            mar = each[1]
if mar >= m:
    print('YES')
else:
    print('NO')

