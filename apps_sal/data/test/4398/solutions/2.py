N = int(input())
S, T = input().split()

answer = ''

for i in range(0, N):
    answer += S[i] + T[i]

print(answer)
