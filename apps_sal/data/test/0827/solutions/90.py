N = int(input())
T = input()
S = "110" * 10**6

if T == "0":
    print(10**10)
elif T == "1":
    print(2 * 10**10)
elif T == "11":
    print(10**10)
else:
    for i in range(3):
        if S[i:N + i] == T:
            print(10**10 - ((N + 2) // 3 - 1) - ((i + N + 2) // 3 > (N + 2) // 3))
            return
    print(0)
