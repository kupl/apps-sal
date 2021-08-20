N = int(input())
(S, T) = map(str, input().split())
s_list = list(S)
t_list = list(T)
answer = []
for i in range(0, N):
    answer.append(S[i])
    answer.append(T[i])
print(''.join(answer))
