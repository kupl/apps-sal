N = int(input())
number_list = list(map(int, input().split(' ')))
ret = [0, 9999999]
for n in range(1, 101):
    temp = 0
    for number in number_list:
        temp += max(0, abs(number - n) - 1)
    if ret[1] > temp:
        ret[0] = n
        ret[1] = temp

print(ret[0], ret[1])
