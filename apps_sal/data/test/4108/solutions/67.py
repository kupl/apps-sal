import sys

input = sys.stdin.readline
S = input().strip()
T = input().strip()

# S -> T
index_s = {}
# T -> S
index_t = {}
for i in range(len(S)):
    if T[i] in index_t:
        if index_t[T[i]] != S[i]:
            print("No")
            return
    else:
        index_t[T[i]] = S[i]

    if S[i] in index_s:
        if index_s[S[i]] != T[i]:
            print("No")
            return
    else:
        index_s[S[i]] = T[i]

print("Yes")
