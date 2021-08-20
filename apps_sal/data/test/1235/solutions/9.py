def R():
    return map(int, input().split())


n = int(input())
A = sorted(R())
m = int(input())
B = sorted(R())
print(A[n - 1], B[m - 1])
