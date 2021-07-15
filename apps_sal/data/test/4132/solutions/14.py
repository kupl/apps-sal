# 62 C - Monsters Battle Royale
import math
import functools
N = int(input())
A = list(map(int,input().split()))

# すべての要素の GCD
ans = functools.reduce(math.gcd,A)
print(ans)
