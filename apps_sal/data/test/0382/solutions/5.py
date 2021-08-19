(n, m, q) = list(map(int, input().split()))
s = str(input())
t = str(input())
arrx = []
i = 0
count = 0
while i < n:
    if s[i] == t[0]:
        j = 0
        while j + i < n and j < m and (s[j + i] == t[j]):
            j += 1
        if j == len(t):
            count += 1
    arrx.append(count)
    i += 1
for i in range(q):
    (x, y) = list(map(int, input().split()))
    if y - x < m - 1:
        print(0)
    elif x == 1:
        print(arrx[y - m])
    else:
        print(arrx[y - m] - arrx[x - 2])
