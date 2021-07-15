n, x = (int(i) for i in input().split())
list_m = [int(input()) for i in range(0, n)]
tmp = x - sum(list_m)
print(n + tmp // min(list_m))
