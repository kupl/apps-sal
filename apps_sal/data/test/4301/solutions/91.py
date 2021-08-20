import copy
N = int(input())
ary = []
for _ in range(N):
    ary.append(int(input()))
ary_copy = copy.copy(ary)
ary_copy.sort()
max_1 = ary_copy[-1]
max_2 = ary_copy[-2]
for i in ary:
    if i == max_1:
        print(max_2)
    elif i != max_1:
        print(max_1)
