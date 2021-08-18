def solve(a, b, f, k):
    cur_b = b
    cur_k = 0
    refueling_count = 0

    can_0f = cur_b - f >= 0
    if not can_0f:
        return refueling_count, cur_k
    else:
        cur_b -= f

    while cur_k < k:
        faf_path = 2 * (a - f)
        can_faf = cur_b - faf_path >= 0
        can_faf_with_refueling = b - faf_path >= 0
        can_fa = cur_b - (a - f) >= 0
        can_fa_with_refueling = b - (a - f) >= 0
        if can_faf and k - cur_k > 1:
            cur_b = cur_b - faf_path
            cur_k += 1
        elif can_faf_with_refueling and k - cur_k > 1:
            refueling_count += 1
            cur_b = b - faf_path
            cur_k += 1
        elif can_fa:
            cur_k += 1
            return refueling_count, cur_k
        elif can_fa_with_refueling:
            cur_k += 1
            refueling_count += 1
            return refueling_count, cur_k
        else:
            return refueling_count, cur_k

        if cur_k == k:
            return refueling_count, cur_k

        f0f_path = 2 * f
        can_f0f = cur_b - f0f_path >= 0
        can_f0f_with_refueling = b - f0f_path >= 0
        can_f0 = cur_b - f >= 0
        can_f0_with_refueling = b - f >= 0
        if can_f0f and k - cur_k > 1:
            cur_b = cur_b - f0f_path
            cur_k += 1
        elif can_f0f_with_refueling and k - cur_k > 1:
            refueling_count += 1
            cur_b = b - f0f_path
            cur_k += 1
        elif can_f0:
            cur_k += 1
            return refueling_count, cur_k
        elif can_f0_with_refueling:
            cur_k += 1
            refueling_count += 1
            return refueling_count, cur_k
        else:
            return refueling_count, cur_k
    return refueling_count, cur_k


def main():
    a, b, f, k = map(int, input().split())

    refueling_count, cur_k = solve(a, b, f, k)
    if cur_k == k:
        print(refueling_count)
    else:
        print(-1)


main()
