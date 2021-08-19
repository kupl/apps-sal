N = int(input())
a_lst = list(map(int, input().split()))
a_lst.sort(reverse=True)
A_a_lst = []
B_a_lst = []
for i in range(N):
    if i % 2 == 0:
        A_a_lst.append(a_lst[i])
    else:
        B_a_lst.append(a_lst[i])
A_sum = sum(A_a_lst)
B_sum = sum(B_a_lst)
ans = A_sum - B_sum
print(ans)
