x = int(input())
ans = 0
for i in range(1, 100):
    for j in range(2, 10):
        a = i**j
        if a <= x and x-a <= x-ans:
            ans = a
print(ans)
