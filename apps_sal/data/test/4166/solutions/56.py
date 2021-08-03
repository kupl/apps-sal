
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n, m = i_map()
sc = i_row_list(m)
sc.sort()

number = [-1] * n
ch_s = -1
ch_c = -1
ans = -1
for s, c in sc:
    if ch_s == s:
        if ch_c != c:
            number[0] = -2
            break
    else:
        number[s - 1] = c
        ch_s = s
        ch_c = c
if number[0] != 0:
    ans = 0
    if number[0] == -1:
        number[0] = 1
    for i in range(len(number)):
        if number[i] == -2:
            ans = -1
            break
        if number[i] == -1:
            number[i] = 0
        ans += number[i] * (10**(len(number) - i - 1))
if m == 0:
    if n == 1:
        ans = 0
    else:
        ans = 10**(n - 1)
if n == 1 and number[0] == 0:
    ans = 0
print(ans)
