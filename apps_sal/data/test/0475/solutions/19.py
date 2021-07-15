n,m,k = map(int, input().split())
import math
print((math.factorial(n-1) // math.factorial(n-k-1) // math.factorial(k) * m * (m-1) ** k) % 998244353)
