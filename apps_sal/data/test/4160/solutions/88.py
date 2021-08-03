import math
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


x = i_input()
cnt = 0
num = 100
while True:
    if num >= x:
        break
    num += num // 100
    cnt += 1

print(cnt)
