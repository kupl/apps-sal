A123 = list(map(int, input().split()))
ans = 1000

for i, a in enumerate(A123):
    for j, b in enumerate(A123):
        for k, c in enumerate(A123):
            if i != j and j != k and k != i:
                tmp = abs(b - a) + abs(c - b)
                if tmp < ans:
                    ans = tmp

print(ans)
