n = int(input())

a = list(map(int, input().split()))

a.sort()

print("YES" if a[n] > a[n - 1] else "NO")
