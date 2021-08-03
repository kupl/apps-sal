N, K = map(int, input().split())
S = map(int, input().split())

height_list = list(S)
ride_person = 0

for i in height_list:
    if i >= K:
        ride_person += 1

print(ride_person)
