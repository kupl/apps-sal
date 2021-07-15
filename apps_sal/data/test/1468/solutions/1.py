from sys import stdin,stdout
n=int(stdin.readline())
A = [0] * n
for j in range(n):
    A[j] = stdin.readline().strip()
answer = [0] * n
answer[-1] = A[-1]
for j in range(n-2,-1,-1):
    if A[j] <= answer[j+1]:
        answer[j] = A[j]
    else:
        for i in range(min(len(answer[j+1]),len(A[j]))):
            if A[j][i] > answer[j+1][i]:
                i-=1
                break
        answer[j] = A[j][:i+1]
print('\n'.join(answer))
