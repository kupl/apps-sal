n, k = input().split()
n = int(n)
k = int(k)

w = input().split()
w = [int(i) for i in w]


if n == 1:
    print(w[0] + k)

else:
    w = sorted(w)
    idx = len(w) // 2 + 1
    mul = 1
    gain = 0

    for i in range(idx - 1, len(w) - 1):
        d = w[i + 1] - w[i]
        if k > d * mul:
            # remainder
            k = k - d * mul
            gain += d
        else:
            gain += k // mul
            k = k - d * mul
            break

        mul += 1
    # if for last elt
    if k > 0:
        gain += k // mul

    print(w[idx - 1] + gain)
