def hantei(n, k, m, a_sum):
    if a_sum / n >= m:
        return 0
    if (a_sum + k) / n >= m:
        return m * n - a_sum
    return -1


(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
a_sum = sum(a)
print(hantei(n, k, m, a_sum))
