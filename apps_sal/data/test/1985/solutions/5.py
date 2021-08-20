(k, n) = list(map(int, input().split()))
a = []
b = []
temp = input().split()
s = 0
for i in range(k):
    s += int(temp[i])
    a.append(s)
list.sort(a)
temp = input().split()
for i in range(n):
    b.append(int(temp[i]))
list.sort(b)
count = 0
visit = set()
for i in range(k - n + 1):
    dif = b[0] - a[0]
    if dif not in visit:
        visit.add(dif)
        add = True
        index = 0
        for j in range(n):
            while index < len(a):
                if a[index] == b[j] - dif:
                    break
                elif a[index] > b[j] - dif:
                    add = False
                    break
                else:
                    index += 1
            if index >= len(a):
                add = False
                break
            if not add:
                break
        if add:
            count += 1
    a = a[1:]
print(count)
