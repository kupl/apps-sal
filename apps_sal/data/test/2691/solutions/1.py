(N, P) = map(int, input().split())
S = [i == 'd' for i in input().strip()]


def calcMax(ar):
    j = c = ans = 0
    for i in range(len(ar)):
        while j < len(ar) and c + ar[j] <= P:
            c += ar[j]
            j += 1
        ans = max(ans, j - i)
        c -= ar[i]
    return ans


print(max(calcMax(S), calcMax([not _ for _ in S])))
