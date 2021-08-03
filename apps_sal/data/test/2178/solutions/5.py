def main():
    n = int(input())

    arr = list(map(int, input().split()))
    numb = [0 for i in range(n + 1)]
    for i in range(len(arr)):
        numb[arr[i]] = i + 1

    brr = list(map(int, input().split()))
    ind = 0
    for c in brr:
        total = 0
        num = numb[c]
        if num > ind:
            total = num - ind
            ind = num
        print(total, end=' ')


main()
