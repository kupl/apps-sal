

def submit():
    n = int(input())
    a = [int(e) for e in input().split()]

    l, r = 0, 0
    ans = 0
    curr_xor = 0
    curr_sum = 0
    while r < n:
        curr_xor = curr_xor ^ a[r]
        curr_sum = curr_sum + a[r]

        while curr_xor != curr_sum:
            curr_xor = curr_xor ^ a[l]
            curr_sum = curr_sum - a[l]
            l += 1
        ans += r - l + 1
        r += 1

    print(ans)


submit()
