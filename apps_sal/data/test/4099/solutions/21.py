n, k, m = (int(n) for n in input().split())
list_a = [int(n) for n in input().split()]
if n * m <= sum(list_a) + k and n * m - sum(list_a) > 0: print((n * m - sum(list_a)))
elif n * m - sum(list_a) <= 0: print("0")
else: print("-1")

