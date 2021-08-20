N = int(input())
(S, T) = input().split()
str_list = []
for i in range(N):
    str_list += (S[i], T[i])
print(''.join(str_list))
