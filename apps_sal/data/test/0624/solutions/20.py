from math import floor

n, k, m = map(int, input().split())
a = [int(x) for x in input().split()]

if n == 1:
    print(a[0] + min(k, m))
else:
    a = sorted(a, reverse=True)

    if n >= 2:
        breaking = True
        firstly = True
        N = n
        sum_a = sum(a[0:N])

        if m >= N*k:
            score = (sum_a + N*k) / N
        else:
            M = m // k
            r = m % k
            score = (sum_a + M*k + r) / N
        
        max_score = score
        while breaking:
            sum_a = sum_a - a[N-1]
            N = N - 1
            m = m - 1
            if N == 1:
                new_score = a[0] + min(k, m)
            else:
                if m >= N*k:
                    new_score = (sum_a + N*k) / N
                else:
                    M = m // k
                    r = m % k
                    new_score = (sum_a + M*k + r) / N

            if new_score > max_score:
                max_score = new_score
            if N == 1 or m == 0:
                breaking = False

            score = new_score
        print(max_score)
