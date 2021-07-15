from sys import stdin
input = stdin.readline

def Judge(N, S):
    for i in range(N-1):
        if S[i] == S[i+1]:
            return i+1, i+2
    for i in range(N-2):
        if S[i] == S[i+2]:
            return i+1, i+3
    else:
        return -1, -1

S = list(input().strip())
N = len(S)
a, b = Judge(N, S)
print(a, b)
