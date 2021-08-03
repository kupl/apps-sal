n, k = list(map(int, str.split(input())))
cities = tuple(map(int, str.split(input())))
capitales = set([int(s) - 1 for s in str.split(input())])

total_weight = sum(cities)
capitales_weight = sum(map(cities.__getitem__, capitales))
weight = 0
for i in range(n):

    if i in capitales:

        sub_weight = total_weight - capitales_weight
        next_city = (i + 1) % n
        if next_city not in capitales:

            sub_weight -= cities[next_city]

    else:

        sub_weight = cities[(i - 1) % n]

    weight += sub_weight * cities[i]

past_sub_weight = 0
for i in sorted(capitales):

    weight += past_sub_weight * cities[i]
    past_sub_weight += cities[i]

print(weight)
