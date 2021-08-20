N = int(input())
for i in range(int(N ** 0.5) + 1):
    if N >= i ** 2:
        ans = i ** 2
    else:
        break
print(ans)
