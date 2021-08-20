N = int(input())
A_list = [int(i) for i in input().split()]
Total_list = []
s = 0
for num in A_list:
    s += num
    Total_list.append(s)
L = 0
R = 2
ans = Total_list[N - 1] + 1
for Mid in range(1, N - 2):
    sum_L = Total_list[Mid]
    sum_R = Total_list[N - 1] - sum_L
    while abs(sum_L - 2 * Total_list[L]) > abs(sum_L - 2 * Total_list[L + 1]):
        L += 1
    while abs(Total_list[N - 1] - Total_list[R] - (Total_list[R] - sum_L)) > abs(Total_list[N - 1] - Total_list[R + 1] - (Total_list[R + 1] - sum_L)):
        R += 1
    P = Total_list[L]
    Q = sum_L - Total_list[L]
    S = Total_list[R] - sum_L
    T = Total_list[N - 1] - Total_list[R]
    ans = min(ans, max(P, Q, S, T) - min(P, Q, S, T))
print(ans)
