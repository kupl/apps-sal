N,K = map(int,input().split())
H = [int(x) for x in input().split()]
H_sort = sorted(H,reverse=True)
print(sum(H_sort[K:]))
