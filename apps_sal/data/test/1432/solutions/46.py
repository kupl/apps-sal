N = int(input())
A = list(map(int, input().split()))
S = sum(A)
damu_sum = sum(A[1::2])
ans = S - 2 * damu_sum
ans_list = [ans]
for i in range(N - 1):
    ans = 2 * A[i] - ans
    ans_list.append(ans)
print(*ans_list)
