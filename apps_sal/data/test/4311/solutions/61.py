s = int(input())
arr = []
ans = 0


def calc(n, cnt):
    arr.append(n)

    if cnt >= 1000000:
        return n

    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(3 * n + 1)

    if n in arr:
        return cnt

    cnt += 1
    calc(n, cnt)


calc(s, 0)
print((len(arr) + 1))
