import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    bn = list(bin(N))[2:]
    bn.reverse()
    res = 0
    for i in range(len(bn)):
        res += (bn[i] == "1") * (pow(2, i + 1) - 1)
    print(res)
