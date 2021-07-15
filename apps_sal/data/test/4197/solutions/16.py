N = int(input())
A_list = list(map(int, input().split()))
B_list = [0] * N
for i, A in enumerate(A_list):
    B_list[A_list[i] - 1] = str(i + 1)
ans = " ".join(B_list)
print(ans)
