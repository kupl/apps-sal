def main():
    n = int(input())
    s = input()
    k = input()
    arr = [0] + [ord(s[i]) + ord(k[i]) - 2 * ord('a')for i in range(n)]
    for i in range(n, -1, -1):
        if arr[i] >= 26:
            arr[i] -= 26
            arr[i - 1] += 1
    for i in range(n, -1, -1):
        if arr[i] % 2:
            arr[i + 1] += 13
        arr[i] //= 2
    for i in range(n + 1):
        arr[i] = chr(arr[i] + ord('a'))
    print(''.join(arr[1:]))
    return 0


main()
