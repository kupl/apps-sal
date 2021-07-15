def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    m = sum(A)
    d = []
    for i in range(1, int(m**0.5)+1):
        if m % i == 0:
            d.append(i)
            if i != m // i:
                d.append(m//i)
    d.sort(reverse=True)
    for j in d:
        if j > K + max(A):
            continue
        l = []
        for i in A:
            l.append(i % j)
        t = N - sum(l) // j
        l.sort()
        if sum(l[:t]) <= K:
            print(j)
            return
    print((1))
main()

