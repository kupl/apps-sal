N = int(input())
(S, T) = input().split()
answer = []
for i in range(0, N):
    answer.append(S[i] + T[i])
print(''.join(answer))
