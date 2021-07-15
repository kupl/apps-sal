n = int(input())

d = {}

for x in range(n):
    if x == 0:
        L, R = map(str, input().split())
        R = int(R)
        l = L
        r = R
        if not (l, int(r)) in d:
            d[(l, int(r))] = []
        m = int(input())
        for y in range(m):
            l1, r1 = map(str, input().split())
            d[(l, int(r))].append((l1, int(r1)))
        if x != n - 1:
            s = input()
    else:
        l, r = map(str, input().split())
        if not (l, int(r)) in d:
            d[(l, int(r))] = []
        m = int(input())
        for y in range(m):
            l1, r1 = map(str, input().split())
            d[(l, int(r))].append((l1, int(r1)))
        if x != n - 1:
            s = input()

lst = []
array = [L]

#print(d)
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

print(len(lst))
lst.sort()
for (a, b) in lst:
    print(a, b)
