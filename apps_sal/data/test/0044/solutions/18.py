(d, k, a, b, t) = list(map(int, input().split()))


def main():
    if d <= k:
        return d * a
    else:
        ans = a * k
        p = k
        if b * k <= t + k * a:
            ans += (d - k) * b
        else:
            pp = (d - k) // k
            p += pp * k
            ans += pp * (t + k * a)
            if (d - p) * b < t + (d - p) * a:
                ans += (d - p) * b
            else:
                ans += t + (d - p) * a
        return ans


print(main())
