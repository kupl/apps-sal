X = int(input())
ans = 1
for i in range(2, 32):
    for j in range(2, 10):
        if i ** j > X:
            continue
        ans = max(ans, i ** j)
print(ans)
