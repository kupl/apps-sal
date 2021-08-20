def list_int_input(inp):
    return list(map(int, inp.split()))


def int_input(inp):
    return int(inp)


def string_to_list_input(inp):
    return list(inp)


n = int(input())
lst = list(map(int, input().split()))
minn = min(lst)
summ = sum(lst)
sum1 = summ
val = -1
for i in range(50, 1, -1):
    for j in lst:
        if j % i == 0:
            val = i
            sum1 = min(summ - minn - j + int(j / i) + i * minn, sum1)
print(sum1)
