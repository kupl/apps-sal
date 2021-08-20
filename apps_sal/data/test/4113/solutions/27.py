N = int(input())
cake = 4
donuts = 7
ans = 'No'
for i in range(N // donuts + 1):
    reminder = N - i * donuts
    if reminder % cake == 0 or reminder == 0:
        ans = 'Yes'
        break
print(ans)
