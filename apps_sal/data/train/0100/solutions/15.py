import sys

# sys.stdin = open("in.txt")
for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    print((a + b + c - max(0, c - (a + b))) // 2)
    # res = min(a, b)
    # a -= res
    # b -= res
    # res2 = min(b, c)
    # b -= res2
    # c -= res2
    # res3 = min(a, c)
    # a -= res3
    # c -= res3
    # print(res + res2 + res3)
