import sys
input = sys.stdin.readline
N = int(input())
aa = input()[: -1]
ab = input()[: -1]
ba = input()[: -1]
bb = input()[: -1]
mod = 10 ** 9 + 7
if N <= 3:
    print(1)
    return
if ab == "A":
    if aa == "A":
        print(1)
        return
    else:
        if ba == "B":
            print(pow(2, N - 3, mod))
            return
        else:
            table = [0] * (N + 1)
            table[2] = 1
            for i in range(1, N - 1): table[i + 2] = table[i + 1] + table[i]
            print(table[N] % mod)
            return
if ab == "B":
    if bb == "B":
        print(1)
        return
    else:
        if ba == "A":
            print(pow(2, N - 3, mod))
            return
        else:
            table = [0] * (N + 1)
            table[2] = 1
            for i in range(1, N - 1): table[i + 2] = table[i + 1] + table[i]
            print(table[N] % mod)
            return
