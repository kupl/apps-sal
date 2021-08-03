def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


X = i_input()
cnt500 = X // 500
cnt5 = (X - cnt500 * 500) // 5
print((cnt500 * 1000 + cnt5 * 5))
