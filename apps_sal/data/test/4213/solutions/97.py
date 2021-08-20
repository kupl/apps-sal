n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(abs(a[n - 1] - a[0]))
