def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    CAA = input()
    CAB = input()
    CBA = input()
    CBB = input()
    if N == 2:
        print(1)
        return
    fibs = [1, 2]
    for _ in range(N):
        fibs.append((fibs[-1] + fibs[-2]) % MOD)
    if CAB == 'A' and CAA == 'A' or (CAB == 'B' and CBB == 'B'):
        print(1)
    elif CAA == 'B' and CAB == CBA == 'A' or (CBB == 'A' and CAB == CBA == 'B'):
        print(fibs[N - 3])
    else:
        print(pow(2, N - 3, MOD))


main()
