from collections import Counter

N = int(input())
s = [input() for _ in range(N)]
 
# N=10^5より、O(N)で解く
# ソート（さらに扱いやすくするため、文字列に直す）することで、文字分布を得る
for i in range(N):
  s[i] = ''.join(sorted(s[i]))

# 文字分布が同じになる組み合わせの個数を求めればよい
# 各文字分布の出現個数nに対して、nC2の和を取る
s = Counter(s).most_common()
ans = 0
for p in s:
  ans += p[1] * (p[1]-1) // 2
  
print(ans)
