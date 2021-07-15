n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
cnt = 0
for z in range(-100, 101):
    if X < z and z <= Y and max(x) < z and min(y) >= z:
        print("No War")
        break
    else:
        cnt += 1
        if cnt == 201:
            print("War")
            break
