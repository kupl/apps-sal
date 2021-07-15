# ABC 133 D
N = int(input())
A_list = list(map(int, input().split()))
x_list = [0] * N
x_list[0] = sum(A_list) - sum([2*a for a in A_list[1::2]])
for i, a in enumerate(A_list[:-1]):
    x_list[i+1] = 2*a - x_list[i]

print(*x_list)
