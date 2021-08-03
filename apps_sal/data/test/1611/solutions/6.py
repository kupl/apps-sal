n = int(input())
A = [int(x) for x in input().split()]
print(2 * max(A) - sum(A) + 1)
