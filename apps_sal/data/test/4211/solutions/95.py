n = int(input())
B = list(map(int, input().split()))
A = [B[0]]
for i in range(n - 2):
    A.append(min(B[i], B[i + 1]))
A.append(B[-1])
print(sum(A))
