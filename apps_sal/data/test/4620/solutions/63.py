N = int(input())
station = [list(map(int, input().split())) for _ in range(N - 1)]

lst = []

for i in range(N - 1):
    c, s, f = station[i]

    for j in range(len(lst)):
        a = lst[j]

        if a >= s:
            if a % f == 0:
                a += c
            else:
                a += (f - a % f) + c
        else:
            a = s + c

        lst[j] = a

    lst.append(s + c)


lst.append(0)
for a in lst:
    print(a)
