N = int(input())
S = list(input())
T = [ord(i) for i in S]
for i in range(len(S)):
    T[i] += N
    if T[i] > 90:
        T[i] -= 26
U = [chr(i) for i in T]
print(''.join(U))
