X = int(input())

i = 2

ans = 1
while i < X:
    power = 2
    while i**power <= X:
        ans = max(ans, i**power)
        power += 1
    i += 1
print(int(ans))
