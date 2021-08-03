def nod(a, b):
    if (b == 0):
        return a
    else:
        return nod(b, a % b)


def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    no = 0
    for i in range(1, n):
        no = nod(arr[i] - arr[i - 1], no)
    ans = 0
    for i in range(1, n):
        ans += -1 + (arr[i] - arr[i - 1]) // no
    print(ans)


main()
