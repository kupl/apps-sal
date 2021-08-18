from collections import defaultdict

chef_country = defaultdict(str)
country = defaultdict(int)
name = defaultdict(int)

a, b = list(map(int, input().split()))
c, n = 0, 0
country_name, chef_name = [], []

for i in range(a):
    p, q = list(map(str, input().split()))
    chef_country[p] = q

for i in range(b):
    q = input()
    country[chef_country[q]] += 1
    name[q] += 1
    if country[chef_country[q]] > c:
        c = country[chef_country[q]]
        country_name = [chef_country[q]]

    elif country[chef_country[q]] == c:
        country_name.append(chef_country[q])

    if name[q] > n:
        n = name[q]
        chef_name = [q]

    elif name[q] == n:
        chef_name.append(q)

country_name.sort()
chef_name.sort()

print(country_name[0])
print(chef_name[0])
