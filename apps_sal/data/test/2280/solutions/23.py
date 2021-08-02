test_count = int(input())
for _ in range(test_count):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(max(min(n - 2, arr[-2] - 1), 0))
