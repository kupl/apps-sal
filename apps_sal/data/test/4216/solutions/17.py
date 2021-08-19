N = int(input())


def divisors(N):
    result = 1e12
    for i in range(2, N):
        if i**2 > N:
            break
        if N % i == 0:
            B = int(N / i)
            tmp = max(len(str(B)), len(str(i)))
            result = min(result, tmp)
    # 自身でしか割れない
    if result == 1e12:
        result = len(str(N))
    return result


print((divisors(N)))
