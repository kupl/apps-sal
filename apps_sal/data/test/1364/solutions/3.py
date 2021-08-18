

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    pre = []
    st = 0
    for ed in range(n):
        while nums[st] != nums[ed]:
            st += 1
        pre.append(st - 1)
    ans = 0
    for i in range(n):
        if pre[i] != -1:
            ans = max(ans, min(i - pre[i], pre[i] - pre[pre[i]]))
    print(ans + ans)


def __starting_point():
    main()


__starting_point()
