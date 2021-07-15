N, K = map(int, input().split())
H = map(int, input().split())
height_list = list(H)

ride = 0

for i in height_list:
    if i >= K:
        ride += 1

print(ride)
