3.5
n = int(input())
A = [int(s) for s in input().split(' ') if s != '']
ret = 0
for i in range(1, len(A) - 1):
    if A[i] == 0 and A[i - 1] == 1 and (A[i + 1] == 1):
        A[i + 1] = 0
        ret += 1
print(ret)
