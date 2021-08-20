n = int(input())
a = sorted(map(int, input().split()))
ans = a[::2] + a[n - 1 - n % 2::-2]
print(' '.join(map(str, ans)))
