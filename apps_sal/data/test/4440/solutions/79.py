
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int,input().split())) for _ in range(N)]

l=i_input()
print((l/3)**3)
