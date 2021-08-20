N = int(input())
(S, T) = map(str, input().split())
res_list = []
for a in range(N):
    res_list.append(S[a])
    res_list.append(T[a])
    a += 1
print(''.join(res_list))
