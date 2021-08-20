import sys


def main():
    (n, x, d) = list(map(int, input().split()))
    events_map = {}
    if d == 0:
        if x == 0:
            print(1)
        else:
            print(n + 1)
        return
    for k in range(n + 1):
        l = (k * x if d > 0 else -k * x) + (k - 1) * k // 2 * abs(d)
        r = (k * x if d > 0 else -k * x) + (n - k + n - 1) * k // 2 * abs(d)
        row = l % abs(d)
        if row not in events_map:
            events_map[row] = []
        events_map[row].append((l, -1))
        events_map[row].append((r, 1))
    ans = 0
    for q in list(events_map.items()):
        events = q[1]
        events.sort()
        bal = 0
        total = 0
        curL = -1
        for event in events:
            if bal == 0 and event[1] == -1:
                curL = event[0]
            if bal == 1 and event[1] == 1:
                curr = event[0]
                total += (curr - curL) // abs(d) + 1
            bal -= event[1]
        ans += total
    print(ans)


main()
