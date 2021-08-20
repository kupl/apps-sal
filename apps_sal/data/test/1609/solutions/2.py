def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = [0] * n
    for i in range(n):
        if a[i] > n or d[a[i] - 1] == 1:
            a[i] = -1
        else:
            d[a[i] - 1] = 1
    for s in range(n):
        if d[s] == 0:
            break
    for i in a:
        if i == -1:
            print(s + 1, end=' ')
            for s in range(s + 1, n):
                if d[s] == 0:
                    break
        else:
            print(i, end=' ')


main()
