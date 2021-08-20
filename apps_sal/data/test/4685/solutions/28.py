(A, B, C) = map(int, input().split())
K = int(input())
n_list = [A, B, C]
x = max(n_list)
n_list.append(x * 2 ** K)
n_list.remove(x)
print(sum(n_list))
