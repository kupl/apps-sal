from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    if N % 2 == 1:
        ans = 'Second'
    elif all((v % 2 == 0 for v in list(C.values()))):
        ans = 'Second'
    else:
        ans = 'First'
    print(ans)
