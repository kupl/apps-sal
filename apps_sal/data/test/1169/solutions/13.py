n, m = list(map(int, input().split()))

min_v = max(0, n - m * 2)

in_clique = 1
while m > 0:
    m -= in_clique
    in_clique += 1

max_v = n - in_clique + (in_clique == 1)



print(min_v, max_v)

