input()
A = list(map(int, input().split()))
max_A = 0
sum_A = 0
for Ai in A:
    max_A = max(Ai, max_A)
    if max_A > Ai:
        sum_A += max_A - Ai
print(sum_A)
