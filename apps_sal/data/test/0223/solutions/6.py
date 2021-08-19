def perm(a, b):
    ret = 1
    for i in range(a, a - b, -1):
        ret = (ret * i) % 1000000007
    return ret


num = int(input())
num2 = num
c = 0
while num2:
    c += 1
    num2 >>= 1
pow2 = 1 << (c - 1)
array = [pow2]
for i in range(c - 1):
    array.append(array[-1] >> 1)


def calc(arr):
    data = []
    #sm = 0
    av = num
    for i in range(c):
        data.append((num // arr[i] - (num - av), av))
        av -= data[-1][0]

    # print(data)

    ans = 1
    for d in data:
        ans = (ans * (d[0] * perm(d[1] - 1, d[0] - 1))) % 1000000007
    return ans


answer = calc(array)

if num >= pow2 // 2 * 3:
    for i in range(1, c):
        dat = [1]
        for j in range(1, c):
            if j == i:
                dat = [3 * dat[0]] + dat
            else:
                dat = [2 * dat[0]] + dat
        # print(dat)
        a = calc(dat)
        answer += a

print(answer % 1000000007)
