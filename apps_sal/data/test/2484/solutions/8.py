

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

        # 今のrで実現する最左のlを求める
        while curr_xor != curr_sum:
            curr_xor = curr_xor ^ a[l]
            curr_sum = curr_sum - a[l]
            l += 1
            # 最悪でもr == lで止まる
        ans += r - l + 1
        # rを動かす
        r += 1

    print(ans)


submit()
