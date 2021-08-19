def main():
    n = int(input())
    nums = [i for i in range(2, n + 1)]
    a = [0 for i in range(2, n + 1)]
    cur = 1
    for i in range(n - 1):
        if a[i] == 0:
            a[i] = cur
            index = i
            while index < n - 1:
                a[index] = cur
                index += nums[i]
            cur += 1
    print(' '.join(map(str, a)))


main()
