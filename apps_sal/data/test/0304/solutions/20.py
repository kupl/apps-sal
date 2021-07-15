a = int(input())
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while a != 0:
    b[a % 10] += 1
    a //= 10

ans = 0

def gao(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def shit(n, arr):
    nonlocal ans
    if n == 10:
        sum = 0
        for i in range(10):
            sum += arr[i]
        gg = sum - arr[0]
        gg *= gao(sum - 1)
        for i in range(10):
            if arr[i] > 1:
                gg //= gao(arr[i])
        ans += gg
    else:
        if b[n] > 0:
            for i in range(1, b[n] + 1):
                gg = arr.copy()
                gg.append(i)
                shit(n + 1, gg)
        else:
            arr.append(0)
            shit(n + 1, arr)


shit(0, [])
print(int(ans))
