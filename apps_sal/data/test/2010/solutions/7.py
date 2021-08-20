(n, m) = map(int, input().split())
l = list(map(int, input().split()))
l = [0] + l
l1 = []
for i in range(m):
    l1 += [list(map(int, input().split()))]
k = 0
for i in l1:
    if i[0] == 1:
        l[i[1]] = i[2]
        l[i[1]] -= k
    elif i[0] == 2:
        k += i[1]
    else:
        print(l[i[1]] + k)
