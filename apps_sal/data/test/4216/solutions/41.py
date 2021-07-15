from math import sqrt
from math import floor
n = int(input())
ans = 10 ** 10
for i in range(1,floor(sqrt(n))+1):
    if n % i == 0:
        a = str(i)
        b = str(n // i)
        ans = min(ans,max(len(a),len(b)))
print(ans)
