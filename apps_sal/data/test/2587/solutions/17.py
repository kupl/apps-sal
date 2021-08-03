import math
T = int(input())
for t in range(T):
    n = int(input())
    rem = math.ceil(n / 4)
    ans = ''
    for i in range(n - rem):
        ans += '9'
    for i in range(rem):
        ans += '8'
    print(ans)
