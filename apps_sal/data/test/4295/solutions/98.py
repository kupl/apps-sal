N, K = list(map(int, input().split()))

mod1 = N % K
mod2 = (K - mod1)

print((mod1 if mod1 < mod2 else mod2))
