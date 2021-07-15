def i_input(): return int(input())


def i_map(): return map(int, input().split())


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


k, n = i_map()
aa = i_list()
dif=[]
for i in range(n):
    if i==n-1:
        dif.append(k-aa[-1]+aa[0])
    else:
        dif.append(aa[i+1]-aa[i])
print(k-max(dif))
