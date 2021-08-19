(N, M) = map(int, input().split())


def enum_div(N):
    ret = []
    i = 1
    while True:
        if i ** 2 > N:
            break
        if N % i == 0:
            ret.append(i)
            if i ** 2 != N:
                ret.append(N / i)
        i += 1
    return ret


ans = 0
for i in enum_div(M):
    if i >= N:
        ans = max(ans, M / i)
print(int(ans))
