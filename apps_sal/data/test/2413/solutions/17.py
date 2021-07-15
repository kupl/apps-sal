for rpt in range(int(input())):
    n = int(input())
    layout = input()
    if layout == n * '0':
        print(n)
    else:
        left = 0
        while layout[left] == '0':
            left += 1
        right = n - 1
        while layout[right] == '0':
            right -= 1
        print(2 * max(n - left, right + 1))

