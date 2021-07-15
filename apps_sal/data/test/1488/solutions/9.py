def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = sorted(list(map(int, input().split())))

total_dist = 0
cur_sum = 0
cur_points = 0

for x in a[::-1]:
    total_dist += cur_sum - cur_points * x
    cur_sum += x
    cur_points += 1

total_dist *= 2
total_dist += sum(a)

high = total_dist
low = n
g = gcd(low, high)
print(high // g, low // g)

