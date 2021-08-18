N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True
        AA = [a[j:j + M] for a in A[i:i + M]]
        for a, b in zip(AA, B):
            if a != b:
                flag = False
        if flag:
            print("Yes")
            return
print("No")
