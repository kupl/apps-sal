def main():
    n = int(input())
    # left = []
    # right = []
    arr = []
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))
        # if x > y:
        #     left.append((x, -y))
        # else:
        #     right.append((y, -x))
    ans = 0
    # left.sort(reverse = 1)
    # right.sort(reverse = 1)
    # for i in range(len(left)):
    #     x, y = left[i]
    #     ans += x * i - (n - 1 - i) * y
    # for i in range(len(right)):
    #     x, y = right[i]
    #     ans += x * i - (n - 1 - i) * y
    arr.sort(key=lambda a: a[1] - a[0])
    for i in range(n):
        x, y = arr[i]
        ans += x * i + (n - 1 - i) * y
    print(ans)
    return 0


main()
