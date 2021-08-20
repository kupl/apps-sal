N = int(input())
T = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    (p, x) = tuple(map(int, input().split()))
    tmp_num = T[p - 1]
    T[p - 1] = x
    print(sum(T))
    T[p - 1] = tmp_num
