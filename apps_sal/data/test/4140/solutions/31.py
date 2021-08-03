S = input()

A = [1 if i % 2 == 0 else 0 for i in range(len(S))]
B = [1 if i % 2 != 0 else 0 for i in range(len(S))]

A_cost = 0
B_cost = 0

i = 0

for i in range(len(S)):
    if int(S[i]) != A[i]:
        A_cost += 1
    if int(S[i]) != B[i]:
        B_cost += 1

print(min(A_cost, B_cost))
