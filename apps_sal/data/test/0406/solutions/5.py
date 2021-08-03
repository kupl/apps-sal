n = int(input())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
a = []
i = 0
while i < len(l) - 1:
    #print(l[i], l[i + 1])
    if l[i] == l[i + 1]:
        a.append(l[i])
        i += 2
    else:
        if l[i] == l[i + 1] + 1:
            a.append((l[i] - 1))
            i += 2
        else:
            i += 1

# print(a)
if len(a) % 2 != 0:
    a.append(0)

s, i = 0, 0
while i < len(a):
    s += a[i] * a[i + 1]
    i += 2
print(s)
