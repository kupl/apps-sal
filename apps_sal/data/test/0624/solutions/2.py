(n, k, m) = [int(x) for x in input().split()]
a_is = [int(x) for x in input().split()]
a_is.sort()
total_sum = sum(a_is)
max_avg = (total_sum + min(n * k, m)) / n
for removal in range(1, min(n - 1, m) + 1):
    total_sum -= a_is[removal - 1]
    new_avg = (total_sum + min((n - removal) * k, m - removal)) / (n - removal)
    if new_avg > max_avg:
        max_avg = new_avg
print(max_avg)
