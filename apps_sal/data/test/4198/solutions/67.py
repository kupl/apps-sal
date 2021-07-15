A, B, X = map(int, input().split())

# 二分探索！
# 二分探索とは、自然数Nに対して、単調増加な式f(N)があるとき、
# f(N)<=X を満たす最大のNを求めるアルゴリズム

# 具体的には以下のよう：
# 必ず f(left)<=X を満たす left と、
# 必ず f(right)>X を満たす right を取る
# 以下を繰り返す
# mid=(left+right)/2 に対して、
# f(mid)<=X のとき、left=mid
# f(mid)>X のとき、right=mid
# leftは常にf(left)<=Xを満たし、rightは常にf(right)>Xを満たす
# 最終的に、leftはf(N)<=Xを満たす最大のNに、rightはf(N)>Xを満たす最小のNに、それぞれ収束する

# 今回はf(N)=A*N+B*d(N)
def price(N):
  return A*N + B*len(str(N)) # len(str(N)) => Nの桁数が求まる

left = 0
right = 10 ** 9 + 1
while right - left > 1:
  mid = (left + right) // 2
  if price(mid) <= X: left = mid
  else: right = mid
print(left)
