def main():
    n = int(input())
    a = list(map(int, input().split()))
    right = 0
    now_sum = 0
    now_xor = 0
    ans = 0
    for left in range(n):
        while right < n and a[right] + now_sum == now_xor ^ a[right]:
            now_sum += a[right]
            now_xor ^= a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            now_sum -= a[left]
            now_xor ^= a[left]
    print(ans)


def __starting_point():
    main()

__starting_point()
