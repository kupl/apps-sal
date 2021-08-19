def IntBaseConvert(N, K):
    if type(N) is int and type(K) is int:
        if K >= 2 and N >= 0:
            if N == 0:
                return [0]
            else:
                ConvertNum = []
                while N > 0:
                    ConvertNum.append(N % K)
                    N = N // K
                return ConvertNum[::-1]
        elif K <= -2:
            if N == 0:
                return [0]
            else:
                ConvertNum = []
                while abs(N) > 0:
                    ConvertNum.append(N % abs(K))
                    N = (N - N % abs(K)) // K
                return ConvertNum[::-1]
        else:
            return []
    else:
        return []


ConvertNum = IntBaseConvert(int(input()), -2)
print(''.join((str(T) for T in ConvertNum)))
