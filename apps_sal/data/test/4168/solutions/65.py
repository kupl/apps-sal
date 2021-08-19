def BaseM2Num(N):
    if N == 0:
        return [0]
    else:
        List = []
        while abs(N) > 0:
            if N % 2 == 0:
                N //= -2
                List.append(0)
            else:
                N = (N - 1) // -2
                List.append(1)
        return List[::-1]


List = BaseM2Num(int(input()))
print(''.join((str(T) for T in List)))
