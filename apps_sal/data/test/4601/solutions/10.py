(N, K) = map(int, input().split(' '))
H_ls = list(map(int, input().split(' ')))
H_ls.sort(reverse=True)
print(sum(H_ls[K:]))
