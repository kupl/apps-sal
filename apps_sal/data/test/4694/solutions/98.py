N = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[N - 1] - a[0])
