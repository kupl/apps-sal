N = int(input())
A_ls = []
B_ls = [float('inf')] + list(map(int, input().split(' '))) + [float('inf')]
for i in range(N):
    A_ls.append(min(B_ls[i], B_ls[i + 1]))
print(sum(A_ls))
