n, m = [int(i) for i in input().split()]
top = [int(i) for i in input().split()]
mid = [int(j) for i in range(1, n - 1) for j in input().split()]
bot = [int(i) for i in input().split()]

l = (n - 2) * m
mid = mid[0: l: m] + mid[m - 1: l: m]

print(2) if 1 in top + mid + bot else print(4)
