X = int(input())
ans = 0
for i in range(1, 32):
    for j in range(2, 10):
        tmp = i ** j
        if ans < tmp <= X:
            ans = tmp
print(ans)
