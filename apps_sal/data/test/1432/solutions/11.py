N = int(input())
A = [int(_) for _ in input().split()]

ans = [sum(A) - 2 * sum(A[1::2])]
for a in A[:-1]:
    ans.append(a * 2 - ans[-1])

print((" ".join([str(_) for _ in ans])))

