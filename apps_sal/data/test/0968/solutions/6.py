n = int(input())
name = ['' for i in range(n)]
sname = ['' for i in range(n)]
for i in range(n):
    (name[i], sname[i]) = input().split()
p = list(map(int, input().split()))
for i in range(n):
    p[i] -= 1
nm = [False for i in range(n)]
snm = [False for i in range(n)]
nm[0] = snm[0] = True
for i in range(1, n):
    if nm[i - 1]:
        if name[p[i]] > name[p[i - 1]]:
            nm[i] = True
        if sname[p[i]] > name[p[i - 1]]:
            snm[i] = True
    if snm[i - 1]:
        if name[p[i]] > sname[p[i - 1]]:
            nm[i] = True
        if sname[p[i]] > sname[p[i - 1]]:
            snm[i] = True
print('YES' if snm[-1] or nm[-1] else 'NO')
