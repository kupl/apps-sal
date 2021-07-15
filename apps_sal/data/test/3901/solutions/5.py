import sys
import fractions

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

one_count = 0
for v in data:
    if v == 1:
        one_count += 1

if one_count > 0:
    print(n - one_count)
else:
    ans = -1
    for i in range(0, n):
        v = data[i]
        for j in range(i + 1, n):
            v = fractions.gcd(v, data[j])
            if v == 1:
                cand = j - i + n - 1
                if ans == -1 or cand < ans:
                    ans = cand
    print(ans)

