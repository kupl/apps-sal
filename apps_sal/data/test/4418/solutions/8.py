def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    used = [0 for i in range(n)]
    sh = [4, 8, 15, 16, 23, 42]
    time = 0
    arr = [0 for i in range(6)]
    for i in range(n):
        if a[i] == sh[0]:
            arr[0] += 1
        elif a[i] == sh[1]:
            if arr[0] > 0:
                arr[0] -= 1
                arr[1] += 1
        elif a[i] == sh[2]:
            if arr[1] > 0:
                arr[1] -= 1
                arr[2] += 1
        elif a[i] == sh[3]:
            if arr[2] > 0:
                arr[2] -= 1
                arr[3] += 1
        elif a[i] == sh[4]:
            if arr[3] > 0:
                arr[3] -= 1
                arr[4] += 1
        elif a[i] == sh[5]:
            if arr[4] > 0:
                arr[4] -= 1
                arr[5] += 1
    print(n - (arr[-1] * 6))


main()

