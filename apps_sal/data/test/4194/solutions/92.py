def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]

dnum,hwnum=i_map()
hws=i_list()
if dnum>=sum(hws):
    ans=dnum-sum(hws)
    print(ans)
else:
    print((-1))


