gcd = lambda a, b: gcd(b, a % b) if b else a


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    summ = sum(arr)
    ind = []
    fm, sm = arr[0], -1
    ind_fm = 0
    for i in range(len(arr)):
        if arr[i] > fm:
            fm = arr[i]
            ind_fm = i
    for i in range(len(arr)):
        if arr[i] > sm and i != ind_fm:
            sm = arr[i]
    for i in range(len(arr)):
        if i != ind_fm and summ - arr[i] - fm == fm:
            ind.append(i + 1)
        if i == ind_fm and summ - arr[i] - sm == sm:
            ind.append(i + 1)

    print(len(ind))
    print(*ind)


main()
