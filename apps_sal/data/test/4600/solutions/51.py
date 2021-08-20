(n, m) = map(int, input().split())
l = [0] * n
wcount = 0
acount = 0
for i in range(m):
    (A, B) = input().split()
    a = int(A)
    b = str(B)
    if l[a - 1] != -1 and b == 'WA':
        l[a - 1] += 1
    elif l[a - 1] != -1 and b == 'AC':
        acount += 1
        wcount += l[a - 1]
        l[a - 1] = -1
print(acount, wcount)
