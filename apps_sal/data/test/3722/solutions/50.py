mod = 10**9+7


def fibonacci(n):
    x1 = 1
    x2 = 1
    for _ in range(n-1):
        nx1 = x2 % mod
        nx2 = (x1+x2) % mod
        x1 = nx1
        x2 = nx2
    return(x2)


N = int(input())
s = ""
for i in range(4):
    s += input()
if N == 2:
    print(1)
elif s[1] == "B" and s[3] == "B":
    print(1)
elif s[0] == "A" and s[1] == "A":
    print(1)
elif s == "ABBA" or s == "BAAA" or s == "BAAB" or s == "BBBA":
    print(fibonacci(N-2))
else:
    print(pow(2, N-3, mod))
