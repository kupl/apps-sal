"""input
6
1 2 3 4 5 6

"""
n = int(input())
ans = 1
a = list(map(int, input().split()))
a = sorted(a)
b = a[::2] + a[1::2][::-1]
print(*b)
