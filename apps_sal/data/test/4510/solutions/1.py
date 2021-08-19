(n, k) = map(int, input().split())
a = map(int, input().split())
lt = dict()
timer = 0
for Id in a:
    if Id not in lt:
        lt[Id] = -k
    cur_time = lt[Id]
    if cur_time <= timer - k:
        timer += 1
        lt[Id] = timer
screen = list(lt.items())
screen.sort(key=lambda t: -t[1])
screen = screen[:min(n, k)]
print(len(screen))
for v in screen:
    print(v[0], end=' ')
print()
