mod = 10**9 + 7
N = int(input())
C = {}
C["AA"] = input()
C["AB"] = input()
C["BA"] = input()
C["BB"] = input()
F = [1, 1]
for i in range(N):
    F.append((F[-1] + F[-2]) % mod)
if N <= 3:
    print((1))
elif C["AB"] == "B":
    if C["BB"] == "B":
        print((1))
    else:
        if C["BA"] == "A":
            print((pow(2, N - 3, mod)))
        else:
            print((F[N - 2]))
else:
    if C["AA"] == "A":
        print((1))
    else:
        if C["BA"] == "B":
            print((pow(2, N - 3, mod)))
        else:
            print((F[N - 2]))
