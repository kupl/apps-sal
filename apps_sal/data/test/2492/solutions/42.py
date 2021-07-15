import numpy as np
def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    cnt_neg, cnt_zro, cnt_pos = 0, 0, 0
    neg_a, zro_a, pos_a = [], [], []
    n_ap = neg_a.append
    z_ap = zro_a.append
    p_ap = pos_a.append
    for v in a:
        if v < 0:
            cnt_neg += 1
            n_ap(v)
        elif v == 0:
            cnt_zro += 1
            z_ap(v)
        else:
            cnt_pos += 1
            p_ap(v)
    num_neg_pair = cnt_neg * cnt_pos
    num_pos_pair = cnt_neg*(cnt_neg-1)//2 + cnt_pos*(cnt_pos-1)//2
    num_zro_pair = n*(n-1)//2 - num_neg_pair - num_pos_pair
    if k <= num_neg_pair:
        neg_a = np.array(neg_a)
        pos_a = np.array(pos_a)
        l = -1*10**18
        r = 0
        while l+1 < r:
            p = (l+r)//2
            cnt = np.searchsorted(pos_a, p//neg_a, side="riget").sum()
            result = n*cnt_neg - (cnt + (cnt_neg + cnt_zro)*cnt_neg)
            if result < k:
                l = p
            else:
                r = p
        print(l)
    elif k <= num_neg_pair + num_zro_pair:
        print("0")
    else:
        k -= num_neg_pair + num_zro_pair
        for i in range(len(neg_a)):
            neg_a[i] = -neg_a[i]
        neg_a = np.array(neg_a)
        neg_a = np.sort(neg_a)
        pos_a = np.array(pos_a)
        l = 1
        r = 10**18+1
        while l+1 < r:
            p = (l+r)//2
            cnt_1 = np.searchsorted(neg_a, (p+neg_a-1)//neg_a, side="left").sum()
            cnt_2 = np.searchsorted(pos_a, (p+pos_a-1)//pos_a, side="left").sum()
            cnt_1 -= np.count_nonzero(neg_a < (p+neg_a-1)//neg_a)
            cnt_2 -= np.count_nonzero(pos_a < (p+pos_a-1)//pos_a)
            result = (cnt_1 + cnt_2)//2
            if result < k:
                l = p
            else:
                r = p
        print(l)

def __starting_point():
    main()

__starting_point()
