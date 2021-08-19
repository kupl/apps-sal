import collections
N = int(input())
a = [int(i) for i in input().split()]
check = []
dict = collections.Counter(a)
for (a, b) in dict.items():
    if b >= 2:
        check.append(a)
if len(check) >= 2:
    check.sort()
    if dict[check[-1]] >= 4:
        print(check[-1] ** 2)
    else:
        print(check[-1] * check[-2])
elif len(check) == 1:
    if dict[check[-1]] >= 4:
        print(check[-1] ** 2)
    else:
        print(0)
else:
    print(0)
