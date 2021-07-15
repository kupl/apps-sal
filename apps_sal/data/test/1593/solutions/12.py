from math import sqrt

class City:
    def __init__(self, x, y, pop):
        self.distance = sqrt(x*x + y*y)
        self.population = pop

n, need = list(map(int, input().split()))
need = 1000000 - need
cities =[]
total = 0
for i in range(n):
    x, y, pop = list(map(int,input().split()))
    cities.append(City(x,y,pop))
    total += pop

if total < need:
    print(-1)
else:
    cities.sort(key=lambda city: city.distance)
    dis = 0
    i = 0
    while need > 0:
        need -= cities[i].population
        dis = cities[i].distance
        i += 1

    print(dis)





