class City:
    def __init__(self, prefecture, year):
        self.prefecture = prefecture
        self.year = year
        self.order = None

    def __eq__(self, other):
        if self.year == other.year:
            return True
        return False

    def __le__(self, other):
        if self.year <= other.year:
            return True
        return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        return False

    def __ge__(self, other):
        if self.year >= other.year:
            return True
        return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        return False


cities = []
n,m=[int(i) for i in input().split()]
prefecture=[[] for i in range(n+1)]



for i in range(m):
    p,y=[int(j) for j in input().split()]
    new_city=City(p, y)
    cities.append(new_city)
    prefecture[p].append(new_city)

for pref_list in prefecture:
    pref_list.sort()
    for i ,pref in enumerate(pref_list):
        pref.order=i+1

for city in cities:
    print((str(city.prefecture).zfill(6)+str(city.order).zfill(6)))



