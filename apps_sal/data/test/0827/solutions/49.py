N = int(input())
T = input()
S = "110" * (int(N / 3) + 3)

a = S.find(T)
if a == -1:
    print(0)
elif T == "1":
    print(10**10 * 2)
else:
    print(10**10 - int((a + N - 1) / 3))
