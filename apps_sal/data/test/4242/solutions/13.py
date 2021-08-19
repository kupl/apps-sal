(A, B, K) = map(int, input().split())
i_list = []
for i in range(1, A + 1):
    if A % i == 0 and B % i == 0:
        i_list.append(i)
print(i_list[-K])
