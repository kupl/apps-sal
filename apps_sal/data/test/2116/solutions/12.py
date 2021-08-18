n, m, k = list([int(q) for q in input().split()])
k_lst = list([int(q) for q in input().split()])
order_lst = []
for i in range(n):
    lst = list([int(q) for q in input().split()])
    order_lst += lst


def calcCost(n, m, k, k_lst):
    total_min = 0
    _index = 0
    for i in range(n * m):
        _item = order_lst[_index]
        for index, item in enumerate(k_lst):
            if item == _item:
                total_min += index + 1
                break
        k_lst = [k_lst[index]] + k_lst[0:index] + k_lst[index + 1:]
        _index += 1
    return total_min


print(calcCost(n, m, k, k_lst))
