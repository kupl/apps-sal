X = int(input())
ans = 0
for i in range(X + 1):
    if i * i <= X:
        sum = i * i
        for j in range(X):
            if i ** j > X:
                break
            sum = max(sum, i ** j)
    else:
        break
    ans = max(ans, sum)
print(ans)
