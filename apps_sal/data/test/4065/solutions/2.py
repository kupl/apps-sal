"""input
6
4 7 12 100 150 199
"""
n = int(input())
a = list(map(int, input().split()))
s = ''.join(['1' if 2 * a[i] >= a[i + 1] else '0' for i in range(n - 1)])
print(len(max(s.split('0'))) + 1)
