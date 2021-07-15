X = int(input())
ans = 1
for i in range(2, X + 1):
    for j in range(2, X + 1):
        a = i ** j
        if a > X:
            break
        elif a > ans:
            ans = a
print(ans)
