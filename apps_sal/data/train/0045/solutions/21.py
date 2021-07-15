A = [1]
s = 1
for i in range(32):
    s *= 4
    A.append(A[-1] * 2 + s)
S = [0] * 33
for i in range(32):
    S[i+1] = S[i] + A[i]
T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(33):
        if S[i] > N:
            print(i - 1)
            break


