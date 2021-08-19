(A, B, K) = list(map(int, input().split()))
divid_number = []
for X in range(1, 100 + 1):
    if A % X == 0 and B % X == 0:
        divid_number.append(X)
divid_number.reverse()
print(divid_number[K - 1])
