(N, M) = map(int, input().split())
A_B = [tuple(map(int, input().split())) for _ in range(N)]
A_B = sorted(A_B, key=lambda x: x[1], reverse=True)
A_B = sorted(A_B, key=lambda x: x[0], reverse=False)
pay = 0
drink = M
for (A, B) in A_B:
    if drink <= B:
        pay += A * drink
        break
    else:
        pay += A * B
        drink -= B
print(pay)
