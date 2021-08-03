import copy

N = int(input())
list1 = list(map(int, input().split()))
list2 = copy.copy(list1)
list3 = set(list1)


x = len(list2)
y = len(list3)


if x == y:
    print('YES')
else:
    print('NO')
