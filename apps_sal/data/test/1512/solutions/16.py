bit = [0] * 100100


def upd(pos, x):
    while pos < 100100:
        bit[pos] += x
        pos += pos & -pos


def sum(pos):
    res = 0
    while pos > 0:
        res += bit[pos]
        pos -= pos & -pos
    return res


def main():
    n = int(input())
    arr = [0]
    for x in input().split():
        arr.append(int(x))
    pont = [0] * 100100
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(1)
        return
    else:
        maxi = arr[1]
        upd(arr[1], 1)
        pont[arr[1]] = -1
        for i in range(2, n + 1):
            '\t\n            print("sum[",n,"] = ",sum(n))\n            print("sum[",arr[i],"] = ",sum(arr[i]))\n            print()\n            '
            if sum(n) - sum(arr[i]) == 1:
                pont[maxi] += 1
            if sum(n) - sum(arr[i]) == 0:
                pont[arr[i]] -= 1
            upd(arr[i], 1)
            maxi = max(maxi, arr[i])
        resp = -9999999
        for i in range(1, n + 1):
            resp = max(resp, pont[i])
        res = 99999999
        for i in range(1, n + 1):
            if resp == pont[i]:
                res = min(res, i)
        print(res)


main()
