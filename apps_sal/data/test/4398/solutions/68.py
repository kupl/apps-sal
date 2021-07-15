N = int(input())
S, T = map(str, input().split())

result = []
for i in range(N):
    result.append(S[i])
    result.append(T[i])

print(''.join(result))
