n_cases = int(input())
for case_num in range(n_cases):
    (a, b, q) = [int(x) for x in input().split()]
    k = a * b
    pref = [0] * k
    for i in range(1, k):
        pref[i] = pref[i - 1]
        if i % a % b != i % b % a:
            pref[i] += 1
    for (i, query) in enumerate(range(q)):
        (l, r) = [int(x) for x in input().split()]
        count = 0
        if l % k != 0:
            count += pref[k - 1] - pref[l % k - 1]
            l = (l // k + 1) * k
        if r % k != k - 1:
            count += pref[r % k]
            r = r // k * k - 1
        assert (r - l + 1) % k == 0
        count += pref[k - 1] * ((r - l + 1) // k)
        if i > 0:
            print(' ', end='')
        print(count, end='')
    print()
