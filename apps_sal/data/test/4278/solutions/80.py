#他の人の回答
import collections

N = int(input())
s = ["".join(sorted(input())) for _ in range(N)]
#sortedでリストになった文字列をjoinでもう一度文字列に
c = collections.Counter(s)
#cは辞書の形をとる
ans = 0

# sから重複を無くす
for si in set(s):
    n = c[si]
    ans += n * (n - 1) // 2 
    # n C 2を計算
print(ans)

