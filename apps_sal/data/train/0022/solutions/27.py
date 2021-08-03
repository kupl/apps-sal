

T = int(input())

for t in range(T):
    a, K = list(map(int, input().split()))

    for k in range(K - 1):
        a_ar = list(map(int, list(str(a))))

        if min(a_ar) == 0:
            break

        a += min(a_ar) * max(a_ar)

    print(a)
