(n, k) = map(int, input().split())
people = list(sorted(map(int, input().split())))
res = 0
while len(people) != 0:
    x = people[-1]
    i = 0
    while len(people) != 0 and i != k:
        i += 1
        people.pop()
    res += x - 1
    res += x - 1
print(res)
