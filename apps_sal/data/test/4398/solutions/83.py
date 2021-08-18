N = int(input())
S, T = map(str, input().split())


answer = ''
for i in range(N):
    answer += S[i] + T[i]

print(answer)
