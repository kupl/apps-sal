a, b = map(int, input().split())
ans = 0
for i in range(50):
    for j in range(30):
        if ((2**i) * (3**j) >= a) and ((2**i) * (3**j) <= b):
            ans = ans + 1

print(ans)
