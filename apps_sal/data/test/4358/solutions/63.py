n = int(input())
list_p = sorted([int(input()) for n in range(0, n)])
print(sum(list_p[:n - 1]) + list_p[n - 1] // 2)
