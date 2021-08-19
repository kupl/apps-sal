n = int(input())
a = [int(c) for c in input().split()]

kardio = [[]]


# for i in range(len(a)):
#     x += a[i]
#     if i % 2 == 1:
#         y -= a[i]
#     else:
#         y += a[i]
#
#     kardio.append((x,y))
#
# print(kardio)


def add_to_kardio(index, symbol):
    # print('before_add',kardio,index,symbol)
    for i in range(len(kardio)):
        tmp = symbol if i == index else ' '
        kardio[i].append(tmp)
    # print('after_add',kardio)


def add_empty_top(length):
    # print('add_top',length,[' '] * length)
    kardio.insert(0, [' '] * length)


def add_empty_bottom(length):
    kardio.append([' '] * length)


current_x = 0
current_y = -1

for i in range(len(a)):
    if i % 2 == 0:
        current_y += 1
        for t in range(a[i]):
            # print('trying to up: ',current_y)
            current_y -= 1

            if current_y >= 0:
                add_to_kardio(current_y, '/')
            else:
                add_empty_top(current_x)
                current_y = 0
                add_to_kardio(current_y, '/')

            current_x += 1
            # print(kardio)
    else:
        current_y -= 1
        for t in range(a[i]):
            # print('trying to down: ',current_y)
            current_y += 1

            if current_y < len(kardio):
                add_to_kardio(current_y, '\\')
            else:
                add_empty_bottom(current_x)
                add_to_kardio(current_y, '\\')

            current_x += 1
            # print(kardio)

for i in range(len(kardio)):
    print(''.join(kardio[i]))
