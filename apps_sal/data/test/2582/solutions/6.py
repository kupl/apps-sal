n = int(input())
a = [int(x) for x in input().split()]


def Count_Segment(a, n):
    ans = 0
    upto = [0] * (n + 1)
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            curr = a[i]
            j = i - 1
            while j >= 0 and a[j] < curr:
                upto[a[j]] = curr
                j -= 1
            j = i + 1
            while j < n and a[j] < curr:
                if upto[curr - a[j]] == curr:
                    ans += 1
                j += 1
    return ans


print(Count_Segment(a, n))
