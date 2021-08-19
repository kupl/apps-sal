(N, X) = map(int, input().split())
Total = [1]
Patties = [1]
for i in range(1, N + 1):
    Total.append(Total[i - 1] * 2 + 3)
    Patties.append(Patties[i - 1] * 2 + 1)


def Burger(N, X):
    if N == 0:
        if X <= 0:
            return 0
        else:
            return 1
    elif X <= 1 + Total[N - 1]:
        return Burger(N - 1, X - 1)
    else:
        return Patties[N - 1] + 1 + Burger(N - 1, X - 2 - Total[N - 1])


print(Burger(N, X))
