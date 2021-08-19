def main():
    (N, K) = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    i = 1
    pas = [i]
    pas_set = set(pas)
    k = 1
    while k <= K:
        if A[i] in pas_set:
            rps = pas.index(A[i])
            ans = A[i]
            break
        pas.append(A[i])
        pas_set.add(A[i])
        ans = A[i]
        i = A[i]
        k += 1
    if k >= K:
        print(ans)
    else:
        rpnum = (K - rps) % (k - rps)
        print(pas[rps + rpnum])


main()
