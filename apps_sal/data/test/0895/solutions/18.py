n = int(input())
a = [int(i) for i in input().split()]
k = int(input())

j = 1
x = []
c = 0
g = 0
a.sort()
# print(a)
for i in range(n):
    f = i
    j = i + 1
    g = 0
    c = 0
    while g <= k:
        if j == n:
            break
        #print(a[f], a[j])
        if g == k and abs(a[f] - a[j]) != 0:
            break

        elif g + abs(a[f] - a[j]) > k:
            break

        g += abs(a[f] - a[j])
        c += 1
        j += 1
        f += 1
    x.append(c)


# print(x)
print(max(x) + 1)
