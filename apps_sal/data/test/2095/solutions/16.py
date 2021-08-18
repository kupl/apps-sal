
N = int(input())

good_cars = []
for i in range(N):
    collision = list(map(int, input().split()))
    if collision.count(1) + collision.count(3) == 0:
        good_cars.append(i)
print(len(good_cars))
if len(good_cars) != 0:
    print(' '.join([str(x + 1) for x in good_cars]))
