input()
ans = []
cur = 0
status = set()
were = set()
try:
    for ai in map(int, input().split()):
        cur += 1
        if ai < 0:
            status.remove(abs(ai))
            if not status:
                ans.append(cur)
                cur = 0
                were = set()
        else:
            assert ai not in were
            status.add(ai)
            were.add(ai)
    assert not were
    print(len(ans))
    print(*ans)
except (AssertionError, KeyError):
    print('-1')

