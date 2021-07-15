def main():
    n, k = list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    if k == 1:
        print(max(a))
        return 0
    for i in range(n):
        a[i + 1] += a[i]
    maks = [0] * (n - k + 1)
    for j in range(n - k + 1):
        for i in range(n - j - k + 1):
            maks[j] = max(maks[j], a[i + j + k] - a[i])
    mask = 0
    for i in range(n - k + 1):
        mask = max(mask, maks[i] / (k +i))
    print(mask)
    return 0
main()

