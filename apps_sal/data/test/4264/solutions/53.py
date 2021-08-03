# 整数 N が与えられます。 N 以下の正の整数のうち、(先頭に 0 をつけずに十進法で表記したときの) 桁数が奇数であるようなものの個数を求めてください。

N = int(input())

ans = 0

for i in range(1, N + 1):
    S = list(str(i))
    if len(S) % 2 == 1:
        ans += 1
print(ans)
