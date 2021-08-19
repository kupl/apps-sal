from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt_A = Counter(A)
if not all([v == 2 for (k, v) in cnt_A.items() if k != 0]):
    print(0)
else:
    print(pow(2, n // 2, 10 ** 9 + 7))
