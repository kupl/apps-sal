
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


a, b = i_map()
ans = -1
for i in range(1, 2000):
    if (i * 8) // 100 == a and i // 10 == b:
        ans = i
        break
print(ans)
