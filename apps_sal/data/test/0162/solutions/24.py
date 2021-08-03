len_garden = int(input().split()[1])
buckets = [int(a) for a in input().split()]

buckets = sorted(buckets, reverse=True)

for i in buckets:
    if len_garden % i == 0:
        print(int(len_garden / i))
        break
