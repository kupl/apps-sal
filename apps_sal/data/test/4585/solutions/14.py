X = int(input())
sum_i = 0
for i in range(1, 10 ** 5):
    sum_i += i
    if sum_i >= X:
        ans = i
        break
print(ans)
