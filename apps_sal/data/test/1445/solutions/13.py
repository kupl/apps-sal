def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, n // 2, 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
    for i in range(n):
        print(arr[i], end = ' ')
main()
