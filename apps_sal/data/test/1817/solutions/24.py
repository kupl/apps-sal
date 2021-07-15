n = int(input())
a = [int(s) for s in input().split()]
a.sort()
if n % 2 == 0: n -= 1
print(a[n//2])
