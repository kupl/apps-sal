n = int(input())
a = [int(i) for i in input().split()]


# print(n)
# print(a)

sort_a = sorted(a, reverse=True)
# print(sort_a)

now_list = []
next_insert = []
comfort = []
# print('start')
for index, i in enumerate(sort_a):
    if len(now_list) == 0:
        now_list += [i]
        next_insert += [1]
        comfort += [i]
    else:
        if len(next_insert) >= n:
            break
        else:
            next_insert += [1, 1]
            comfort += [i, i]


# print(comfort, next_insert)
print((sum(comfort[:n-1])))

