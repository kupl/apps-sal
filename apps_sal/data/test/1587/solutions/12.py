N = int(input())
C = input()

f = 0
b = N - 1
ans = 0

while True:
    while  f <= N -1 and C[f] == "R":
        f += 1
    while b >= 0 and C[b] == "W":
        b -= 1
    if f > b:
        print(ans)
        break
    ans += 1
    f += 1
    b -= 1
