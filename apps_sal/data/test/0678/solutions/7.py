"""
IM IN YR LOOP NERFIN YR TUX TIL BOTH SAEM TUX AN 0
I HAS A PUR
GIMMEH PUR
PUR IS NOW A NUMBR
FOO R SUM OF FOO AN PUR
BAR R SUM OF BAR AN 1
BOTH SAEM BIGGR OF PRODUKT OF FOO AN QUZ AN PRODUKT OF BAR BAZ AN PRODUKT OF FOO AN QUZ
O RLY?
YA RLY
BAZ R FOO
QUZ R BAR
OIC
IM OUTTA YR LOOP
BAZ IS NOW A NUMBAR
VISIBLE SMOOSH QUOSHUNT OF BAZ QUZ
KTHXBYE
"""
tux, foo, bar, baz, quz = int(input()), 0, 0, 0, 1
while tux != 0:
    pur = int(input())
    foo += pur
    bar += 1
    if max(foo * quz, bar * baz) == foo * quz:
        baz = foo
        quz = bar
    tux -= 1
print(float(baz / quz))
