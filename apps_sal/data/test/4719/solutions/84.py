def main():
    n = int(input())
    s = [input() for i in range(n)]
    nums = [1000 for i in range(26)]
    for i in range(26):
        for j in range(n):
            nums[i] = min(nums[i], s[j].count((chr)(97 + i)))

    for i in range(26):
        while nums[i] > 0:
            print((chr)(97 + i), end="")
            nums[i] -= 1
    print("")


main()
