t = int(input())
for _ in range(t):
    a = sorted(map(int, input().split()))
    print('Yes' if a[0] + a[1] + 1 >= a[2] else 'No')
