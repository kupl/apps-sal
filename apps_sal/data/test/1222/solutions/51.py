L = [1] + [0] * 10
for _ in range(1, int(input())):
    for i in range(10):
        if(L[i] - L[i + 1] < 1 or sum(L[i + 1:]) < 1) and L[i] < 9:
            for j in range(i + 1):
                L[j] = max(L[i] + 1 - i + j, 0)
            break
print(sum(l * 10**i for i, l in enumerate(L)))
