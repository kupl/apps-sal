import math


def isMore(N, K):  # - N以上の数で、０でないのが丁度K個
    # -len(N)よりもKがおおきかったら0
    if len(N) < K:
        return 0
    # 最高位の数字を1つ繰り上げれば、なんでも大きい。ただし、Kは1以上
    if K >= 1:
        tmp = (9 - int(N[0])) * fact[len(N) - 1] // ((fact[len(N) - K]) * (fact[K - 1])) * (9**(K - 1))
        if len(N) == 1:
            return tmp
        elif len(N) > 1 and N[0] == '0':
            return tmp + isMore(N[1:], K)
        elif len(N) > 1 and N[0] != '0':
            return tmp + isMore(N[1:], K - 1)
    if K == 0:
        return 0


N = input()
K = int(input())
lenN = len(N)
fact = [1] * 101
for i in range(1, 101):
    fact[i] = fact[i - 1] * i

ans = fact[lenN] // ((fact[lenN - K]) * fact[K]) * (9**K)
ans -= isMore(N, K)
print(ans)
