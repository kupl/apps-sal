n, p = list(map(int, input().split()))
string = input()


def calc_delta(s):
    """Calculates and returns the alphabetical differences between every pair
    of indices (i, n-i-1) in the string s. Returns a map between an index and
    the delta value to correct to a palindrome.
    """
    def get_min_shift(i):
        ord_diff = abs(ord(s[i]) - ord(s[n - i - 1]))
        return min(ord_diff, 26 - ord_diff)

    return {i: get_min_shift(i) for i in range((n + 1) // 2)}


def palindrome(s):
    deltas = calc_delta(s)
    offset_indices = list([i for i in list(deltas.keys()) if deltas[i] > 0])
    if not offset_indices:
        return 0
    alpha_delta = sum(deltas.values())
    mindex = min(offset_indices)  # Smallest index with a mismatch
    maxdex = max(offset_indices)  # Largest index in the smaller half with a mismatch
    sindex = min(p - 1, n - p)  # Starting pointer index
    if mindex == maxdex or maxdex <= sindex:
        travel_delta = abs(sindex - mindex)
        return travel_delta + alpha_delta
    if mindex >= sindex:
        return maxdex - sindex + alpha_delta
    min_delta = min(maxdex - sindex, sindex - mindex)
    max_delta = max(maxdex - sindex, sindex - mindex)
    travel_delta = 2 * min_delta + max_delta
    return travel_delta + alpha_delta


print(palindrome(string))
