
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(input().split()) for _ in range(N)]


n, m = i_map()
ps = i_row_list(m)
ac = [0] * n
wa = [0] * n
for p, s in ps:
    if s == 'AC':
        ac[int(p) - 1] = 1
    if s == 'WA':
        if ac[int(p) - 1] == 0:
            wa[int(p) - 1] += 1
for i in range(n):
    if ac[i] == 0:
        wa[i] = 0
print(sum(ac), sum(wa))
