N, K = map(int, input().split())
A = list(map(int, input().split()))
c = 0
List = []
check = [-1] * N
tmp = 1
for i in range(min(N + 1, K)):
    tmp2 = A[tmp - 1]
    List.append(tmp2)
    if(check[tmp2 - 1] >= 0):
        tmp3 = check[tmp2 - 1]
        del List[-1]
        break
    else:
        check[tmp2 - 1] = i
        tmp = tmp2
        c += 1
if(c >= K):
    print(List[K - 1])
else:
    List2 = List[tmp3:]
    if(c == len(List2)):
        print(List2[(K % len(List2)) - 1])
    else:
        K -= c
        print(List2[(K % len(List2)) - 1])
