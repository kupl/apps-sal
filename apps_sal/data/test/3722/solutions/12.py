P = 10**9 + 7
N = int(input())
AA = input()
AB = input()
BA = input()
BB = input()
TT = [0]*(N+1)
TT[0] = 1
TT[1] = 1
for i in range(2, N+1):
    TT[i] = (TT[i-1]*i)%P

if AB == "A" and AA == "A":
    print((1))
elif AB == "B" and BB == "B":
    print((1))
elif N <= 3:
    print((1))
elif AB == "A" and AA == "B":
    if BA == "A":
        ans = 0
        for i in range(N//2):
            ans += (((TT[N-2-i]*pow(TT[N-2-2*i], P-2, P))%P)*pow(TT[i], P-2, P))%P
            ans %= P
        print(ans)
    else:
        print((pow(2, N-3, P)))
elif AB == "B" and BB == "A":
    if BA == "B":
        ans = 0
        for i in range(N//2):
            ans += (((TT[N-2-i]*pow(TT[N-2-2*i], P-2, P))%P)*pow(TT[i], P-2, P))%P
            ans %= P
        print(ans)
    else:
        print((pow(2, N-3, P)))


