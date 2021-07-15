from math import sqrt
from bisect import bisect_left

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    st = set()
    for v in range(1, int(sqrt(sum_a))+2):
        if sum_a % v == 0:
            st.add(v)
            st.add(sum_a//v)
    st.remove(1)
    ans = 1
    for target in st:
        a_mod_t = [v % target for v in a]
        a_mod_t.sort()
        for i in range(n-1):
            a_mod_t[i+1] += a_mod_t[i]
        for i in range(n):
            sum_L, sum_R = a_mod_t[i], a_mod_t[-1] - a_mod_t[i]
            len_L, len_R = i+1, n-i-1
            if sum_L == target * len_R - sum_R:
                if sum_L <= k:
                    if ans < target:
                        ans = target
    print(ans)

def __starting_point():
    main()
__starting_point()
