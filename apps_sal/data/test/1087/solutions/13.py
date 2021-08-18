

def submit():
    n, k = (int(e) for e in input().split())
    a = [int(e) for e in input().split()]
    max_bit = 40
    bit_cnt = []

    b = 0
    bit = 1
    while b <= max_bit:
        cnt = sum(e & bit > 0 for e in a)
        bit_cnt.append(cnt)
        bit <<= 1
        b += 1

    isless = False
    curr_bit = 1 << max_bit
    ans = 0
    for i in range(max_bit + 1):
        k_bit = k & curr_bit > 0
        if not isless and k_bit == 0:
            ans += bit_cnt[max_bit - i] * curr_bit
        elif not isless and k_bit == 1:
            cnt1 = bit_cnt[max_bit - i]
            cnt0 = n - cnt1
            if cnt1 > cnt0:
                ans += cnt1 * curr_bit
                isless = True
            else:
                ans += cnt0 * curr_bit
        else:
            cnt1 = bit_cnt[max_bit - i]
            cnt0 = n - cnt1
            if cnt1 > cnt0:
                ans += cnt1 * curr_bit
            else:
                ans += cnt0 * curr_bit
        curr_bit >>= 1

    print(ans)


submit()
