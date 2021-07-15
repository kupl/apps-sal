N = int(input())
T = input()
S = "110" * (N + 2)

if T == "1":
    print(((10 ** 10) * 2))
elif T == "00":
    print((0))
elif N == 2:
    print((10 ** 10 if T != "01" else (10 ** 10) - 1))
elif T in S:
    if S.startswith(T):
        print((10 ** 10 - (N + 2) // 3 + 1))
    elif S[1:].startswith(T):
        print((10 ** 10 - (N + 3) // 3 + 1))
    else:
        print((10 ** 10 - (N + 4) // 3 + 1))
else:
    print((0))

