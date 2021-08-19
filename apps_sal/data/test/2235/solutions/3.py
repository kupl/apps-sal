def main():
    N = int(input())
    S = [0]
    T = [0]
    kh = 0
    kd = 0
    for n in range(1, N + 1):
        T.append(int(input()))
        for i in range(kh + 1, n):
            if T[n] - T[i] < 90:
                kh = i - 1
                break
            else:
                kh = i
        for i in range(kd + 1, n):
            if T[n] - T[i] < 1440:
                kd = i - 1
                break
            else:
                kd = i
        S.append(min(20 + S[n - 1], 50 + S[kh], 120 + S[kd]))
        print(S[n] - S[n - 1])


main()
