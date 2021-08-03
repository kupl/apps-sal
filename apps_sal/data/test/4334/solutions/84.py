S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

print(str(A) + " " + str(B - 1) if T == U else str(A - 1) + " " + str(B))
