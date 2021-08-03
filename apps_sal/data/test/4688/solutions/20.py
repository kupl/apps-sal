lst = input().split()

N = int(lst[0])
K = int(lst[1])

print(K * ((K - 1) ** (N - 1)))
