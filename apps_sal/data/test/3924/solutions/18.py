(n, k) = list(map(int, input().split()))
days = list(map(int, input().split()))
nb_bags = 0
crt_cap = 0
for i in range(n):
    if crt_cap != 0:
        days[i] = max(days[i] - (k - crt_cap), 0)
        crt_cap = 0
        nb_bags += 1
    nb_bags += int(days[i] / k)
    crt_cap = days[i] % k
if crt_cap != 0:
    nb_bags += 1
print(nb_bags)
