N = int(input())
for i in range(100):
    x = 2 ** (100 - i)
    if x <= 64 and x <= N:
        ans = x
        break
    else:
        ans = N
print(ans)
