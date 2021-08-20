t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = arr[::-1]
    print(' '.join(map(str, result)))
