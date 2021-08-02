X = int(input())

L = [0]
for i in range(1, 10 ** 5):
    L.append(L[i - 1] + i)

ans = 0
for i in range(1, X + 1):
    # print(L[i])
    if L[i] >= X:
        ans = i
        break


print(ans)
