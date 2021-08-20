X = int(input())
i = 2
ans = 1
while i < X:
    power = 2
    while power <= X:
        if pow(i, power) <= X:
            ans = max(ans, pow(i, power))
        else:
            break
        power += 1
    i += 1
print(int(ans))
