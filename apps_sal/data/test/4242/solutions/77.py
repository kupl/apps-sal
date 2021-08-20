(A, B, K) = map(int, input().split())
A_list = []
ans_list = []
for i in range(1, A + 1):
    if A % i == 0:
        A_list.append(i)
for n in A_list:
    if B % n == 0:
        ans_list.append(n)
print(ans_list[-K])
