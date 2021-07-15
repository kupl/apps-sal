N = int(input())
Name = [input()[0] for _ in range(N)]
March = {x:Name.count(x) for x in 'MARCH' if Name.count(x) > 0}

import itertools
ans = 0
for x,y,z in itertools.combinations(March.values(), 3):
    ans += x*y*z
print(ans)
