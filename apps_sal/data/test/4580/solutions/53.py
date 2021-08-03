N = int(input())
A = list(map(int, input().split()))
B = [i // 400 for i in A if i < 3200]
if B == []:
    print(1, N)
elif len(B) == N:
    C = len(set(B))
    print(C, C)
else:
    C = len(set(B))
    D = C + N - len(B)
    print(C, D)
