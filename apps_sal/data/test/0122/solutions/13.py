from functools import reduce


def solve():
    sum_ = a[:]
    for i in range(1, n):
        sum_[i] += sum_[i - 1]
    if (sum_[n - 1] % 2): return False
    half = int(sum_[n - 1] / 2)
    st = set([0])
    for i in range(n):
        if sum_[i] >= half and sum_[i] - half in st:
            return True
        st.add(a[i])

    sum_ = a[:]
    for i in range(n - 2, -1, -1):
        sum_[i] += sum_[i + 1]
    st = set([0])
    for i in range(n - 1, -1, -1):
        if sum_[i] >= half and sum_[i] - half in st:
            return True
        st.add(a[i])
    return False


while True:
    try:
        n = int(input())
    except:
        break
    a = [int(x) for x in input().split(' ')]
    print('YES' if solve() else "NO")
