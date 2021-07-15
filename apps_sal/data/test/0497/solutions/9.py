def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = 0
    for i in range(n):
        if arr[i] != arr[-1]:
            m = max(m, n - 1 - i)
            break
    for i in range(n - 1, -1, -1):
        if arr[i] != arr[0]:
            m = max(m, i)
            break
    print(m)
    return 0
main()
