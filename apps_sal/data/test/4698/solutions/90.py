n = int(input())
t_l = list(map(int, input().split()))
m = int(input())
import copy
for _ in range(m):
    k, v = map(int, input().split())
    tmp_t = copy.deepcopy(t_l)
    tmp_t[k-1] = v
    print(sum(tmp_t))
