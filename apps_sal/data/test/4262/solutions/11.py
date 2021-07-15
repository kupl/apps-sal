import itertools
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]

n=i_input()
pp=tuple(i_list())
qq=tuple(i_list())
a,b=-1,-1
for i, rr in enumerate(itertools.permutations(range(1, n + 1))):
    if a==-1 and pp==rr:
        a=i
    if b==-1 and qq==rr:
        b=i
    if a!=-1 and b!=-1:
        break
print(abs(a-b))
