n = int(input())
wl, hl = map(int, input().split())
hl = max(wl, hl)
for i in range(n - 1):
    w, h = map(int, input().split())
    if max(w, h) <= hl:
        hl = max(w, h)
    elif max(w, h) > hl and min(w, h) <= hl:
        hl = min(w, h)
    elif min(w, h) > hl:
        print('NO')
        return
print('YES')
