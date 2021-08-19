A = [int(i) for i in input().split()]
n = A[0]
k = A[1]
S = input()
A = {}
for i in range(26):
    A[chr(97 + i)] = []
for i in range(len(S)):
    A[S[i]].append(i)
for i in range(26):
    A[chr(97 + i)] = A[chr(97 + i)][::-1]
rem = set()
for i in range(26):
    while len(A[chr(97 + i)]) > 0 and k > 0:
        rem.add(A[chr(97 + i)].pop())
        k = k - 1
        if k == 0:
            break
R = ''
for i in range(len(S)):
    if i not in rem:
        R += S[i]
print(R)
