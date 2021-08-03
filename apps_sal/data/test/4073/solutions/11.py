n = int(input())
a = list(map(int, input().split()))
print(max(a) ^ a[n - 1])
