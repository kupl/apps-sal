import itertools


def classify(subset, l, r, x):
    li = []
    for i in subset:
        li.append(i)
    f1 = False
    f2 = False
    f3 = False
    s = 0
    for i in li:
        s += i
    if s >= l:
        f1 = True
    if s <= r:
        f2 = True
    li.sort()
    t = li[len(li) - 1] - li[0]
    if t >= x:
        f3 = True
    if f1 and f2 and f3:
        return True
    else:
        return False


s = input()
s = s.split()
n = int(s[0])
l = int(s[1])
r = int(s[2])
x = int(s[3])

a = input()
a = a.split()
arr = []
for i in a:
    arr.append(int(i))

count = 0
for i in range(2, len(arr) + 1):
    for subset in itertools.combinations(arr, i):
        # print(subset)
        if classify(subset, l, r, x):
            # print(subset)
            count += 1

print(count)
