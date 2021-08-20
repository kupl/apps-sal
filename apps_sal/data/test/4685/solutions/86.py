(m, *A) = sorted([int(x) for x in input().split()], reverse=True)
K = int(input())
print(m * 2 ** K + sum(A))
