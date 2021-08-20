DE = 10 ** 9 + 7
(N, K) = list(map(lambda x: int(x), input().split(' ')))
A = list(map(lambda x: int(x), input().split(' ')))


def main():
    A_posi = []
    A_nega = []
    for a in A:
        if a > 0:
            A_posi.append(a)
        elif a < 0:
            A_nega.append(-a)
    len_posi = len(A_posi)
    len_nega = len(A_nega)
    if len_posi + len_nega < K:
        return 0
    if len_nega % 2 == 1 and K == len_posi + len_nega or (K % 2 == 1 and len_posi == 0):
        if len_posi + len_nega == N:
            A_posi.sort()
            A_nega.sort()
            answer = 1
            k = 0
            for a in A_nega:
                answer *= -a % DE
                answer %= DE
                k += 1
                if k >= K:
                    break
            else:
                for a in A_posi:
                    answer *= a % DE
                    answer %= DE
                    k += 1
                    if k >= K:
                        break
            return answer
        else:
            return 0
    A_posi.sort(reverse=True)
    A_nega.sort(reverse=True)
    posi = 0
    nega = 0
    answer = 1
    if K % 2 == 1:
        answer = A_posi[0] % DE
        posi = 1
    while posi + nega + 2 <= K:
        p = A_posi[posi] * A_posi[posi + 1] if posi + 1 < len_posi else 0
        n = A_nega[nega] * A_nega[nega + 1] if nega + 1 < len_nega else 0
        if p > n:
            answer *= p % DE
            answer %= DE
            posi += 2
        else:
            answer *= n % DE
            answer %= DE
            nega += 2
    return answer


print(main())
