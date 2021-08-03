from collections import Counter
N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
ans = len(count)
if ans % 2 == 0:
    ans -= 1
print(ans)
