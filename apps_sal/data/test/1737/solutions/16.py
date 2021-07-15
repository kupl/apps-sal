n = int(input())

d = {}

for x in range(n):
    l, r = list(map(str, input().split()))
    r = int(r)
    if x == 0:
        L = l
        R = r
    if not (l, r) in d:
        d[(l, r)] = []
    m = int(input())
    for y in range(m):
        l1, r1 = list(map(str, input().split()))
        d[(l, r)].append((l1, int(r1)))
    if x != n - 1:
        s = input()

lst = []
array = [L]
temp1 = [(L, R)]
temp2 = []
k1 = 0
k2 = 1
while k1 < len(temp1) or k2 < len(temp2):
    if k2 > len(temp2):
        while k1 < len(temp1):
            for (a, b) in d[temp1[k1]]:
                temp2.append((a, -b))
            k1 += 1
        temp2.sort()
        temp = []
        for (a, b) in temp2:
            if not a in array:
                array.append(a)
                lst.append((a, -b))
                temp.append((a, -b))
        temp2 = temp[:]
        temp1 = []
        k1 = 1
        k2 = 0
    elif k1 > len(temp1):
        while k2 < len(temp2):
            for (a, b) in d[temp2[k2]]:
                temp1.append((a, -b))
            k2 += 1
        temp1.sort()
        temp = []
        for (a, b) in temp1:
            if not a in array:
                array.append(a)
                lst.append((a, -b))
                temp.append((a, -b))
        temp1 = temp[:]
        temp2 = []
        k2 = 1
        k1 = 0
        
lst.sort()
print(len(lst))
for (a, b) in lst:
    print(a, b)

