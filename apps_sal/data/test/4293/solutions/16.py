P, Q, R = list(map(int, input().split()))

list_m = [P + Q, R + Q, P + R, Q + R, R + P, Q + P]

min = 200
for i in range(0, len(list_m)):
    if min > int(list_m[i]):
        min = list_m[i]

print(min)
