N = int(input())
S, T = input().split()
answer = ""

for i in range(N):
    answer = answer + S[i] + T[i]

print(answer)
