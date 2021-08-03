def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


na, m = i_map()
aa = i_list()
cnt = 0
aa.sort(reverse=True)
for i in range(m):
    if aa[i] * 4 * m >= sum(aa):
        cnt += 1
if cnt == m:
    print('Yes')
else:
    print('No')
