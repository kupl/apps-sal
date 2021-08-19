n = int(input())
one = set()
two = set()
ban = 0
for i in input().split():
    i = int(i)
    if i not in one:
        one.add(i)
    elif i not in two:
        two.add(i)
    else:
        ban = 1
        break
if ban:
    print('NO')
else:
    print('YES')
    one = list(one)
    print(len(one))
    one.sort()
    for i in one:
        print(i, end=' ')
    print()
    two = list(two)
    print(len(two))
    two.sort(reverse=True)
    for i in two:
        print(i, end=' ')
    print()
