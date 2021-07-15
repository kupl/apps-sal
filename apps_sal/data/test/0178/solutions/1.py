def main():
    n = int(input())
    arr = list(map(int, input()))
    a = arr.count(8)
    if a <= (n - 11) // 2:
        print("NO")
        return 0
    i = -1
    cnt = 1 + (n - 11) // 2
    while cnt:
        i += 1
        if arr[i] == 8:
            cnt -= 1
    if i > n - 11:
        print("NO")
        return 0
    print("YES")
    return 0

main()
