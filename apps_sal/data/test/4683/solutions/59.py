MOD = 10 ** 9 + 7  # MODは変数に入れてしまったほうが打ち間違えなくていいです

N = int(input())
A = list(map(int, input().split()))

S = sum(A) % MOD
ans = 0

# A_Nも含まれてしまいますが、そのときはs=0なので問題ありません
for x in A:
    S -= x  # 自分と自分自身を掛けないように、先に引く必要があります
    S %= MOD  # MODはいちいち取っておくといいです
    ans += S * x
    ans %= MOD

ans %= MOD  # この行は完全に不要ですが、最後だけMODを取り忘れてWAになるミスは非常によくあるので、必要以上に取っておくと安心できます
print(ans)
