n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
print(a[(n - 1) // 2])
