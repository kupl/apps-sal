count_per = {}
per = {}
count = {}
s = list(map(int, input().split()))
for i in range(s[0]):
    x = input().split()
    count_per[x[0]] = x[1]
for j in range(s[1]):
    y = input()
    try:
        per[y] += 1
    except:
        per[y] = 1
    try:
        count[count_per[y]] += 1
    except:
        count[count_per[y]] = 1
a = -1
for i, j in count.items():
    if(a < j):
        a = j
        p = i
    elif(a == j):
        if(p > i):
            p = i
print(p)
a = -1
for i, j in per.items():
    if(a < j):
        a = j
        p = i
    elif(a == j):
        if(p > i):
            p = i
print(p)
