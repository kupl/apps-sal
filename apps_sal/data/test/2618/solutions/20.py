from collections import deque
n = int(input())
for _ in range(n):
    m = int(input())
    tickets = list(map(int, input().split()))
    tickets.sort(reverse=True)
    aperc, ajump = map(int, input().split())
    bperc, bjump = map(int, input().split())
    q = int(input())
    if bperc > aperc:
        bperc, aperc = aperc, bperc
        ajump, bjump = bjump, ajump
    aperc = aperc / 100
    bperc = bperc / 100
    zet = False
    ans = -1
    sumo = 0
    da = deque()
    db = deque()
    dc = deque()
    tc = 0
    for i in range(m):
        z = i + 1
        if z % ajump == 0 and z % bjump == 0:
            if(len(da) > 0):
                xx = da.pop()
                dc.appendleft(xx)
                if len(db) > 0:
                    xxx = db.pop()
                    da.appendleft(xxx)
                    db.appendleft(tickets[tc])
                    sumo = sumo + bperc * xx + \
                        (aperc - bperc) * xxx + bperc * tickets[tc]
                else:
                    da.appendleft(tickets[tc])
                    sumo = sumo + bperc * xx + aperc * tickets[tc]

            elif len(db) > 0:
                xx = db.pop()
                dc.appendleft(xx)
                db.appendleft(tickets[tc])
                sumo = sumo + aperc * xx + bperc * tickets[tc]

            else:
                dc.appendleft(tickets[tc])
                sumo = sumo + (aperc + bperc) * tickets[tc]

            tc += 1

        elif z % ajump == 0:
            if len(db) > 0:
                xx = db.pop()
                da.appendleft(xx)
                db.appendleft(tickets[tc])
                sumo = sumo + (aperc - bperc) * xx + bperc * tickets[tc]
            else:
                da.appendleft(tickets[tc])
                sumo = sumo + aperc * tickets[tc]
            tc += 1

        elif z % bjump == 0:
            db.appendleft(tickets[tc])
            sumo = sumo + bperc * tickets[tc]
            tc += 1

        else:
            pass
        if(sumo >= q and (not zet)):
            zet = True
            ans = i + 1
            break

    print(ans)
