t = input
p = print
r = range
(n, k) = map(int, t().split())
cities_beauty = list(map(int, t().split()))
capital = set(map(int, t().split()))
cities = set([i for i in r(1, n + 1)])
cities = cities ^ capital
ans = 0
city_sum = 0
for city in cities:
    if city == 1 and n in cities:
        ans += cities_beauty[0] * cities_beauty[-1]
    if city + 1 in cities and city != n:
        ans += cities_beauty[city - 1] * cities_beauty[city]
    city_sum += cities_beauty[city - 1]
cap_sum = 0
for cap in capital:
    ans += cities_beauty[cap - 1] * city_sum
    cap_sum += cities_beauty[cap - 1]
for cap in capital:
    cap_sum -= cities_beauty[cap - 1]
    ans += cities_beauty[cap - 1] * cap_sum
p(ans)
