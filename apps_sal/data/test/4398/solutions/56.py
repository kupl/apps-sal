N = int(input())
S, T = list(input().split())

new_str = []

for i in range(0, N):
    new_str.append(S[i] + T[i])

print((''.join(new_str)))
