N = {}  # 10000以上key以下の回文数の個数
cnt = 0
for i in range(10000, 100000):
    L = list(str(i))
    if L == list(reversed(L)):
        cnt += 1
    N[i] = cnt
A, B = map(int, input().split())
print(N[B] - N[A - 1] if A > 10000 else N[B])
