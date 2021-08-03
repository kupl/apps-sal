a = int(input())
sa = str(a)
index1 = int(sa[0]) * 1000 + 1000
if a % 1000 == 0:
    print(0)
elif a < 1000:
    print(1000 - a)
elif a > 1000:
    a = index1 - a
    print(a)
