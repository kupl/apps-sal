k = int(input())
I = list(map(int, input().split()))
_00 = []
_01 = []
_11 = []
_10 = []
d = []
for val in I:
    d.append(val)
    if val == 0:
        _00.append(val)
    elif val == 100:
        _00.append(val)
    elif val % 10 == 0:
        _10.append(val)
    elif val < 10:
        _01.append(val)
    else:
        _11.append(val)
_00_ = len(_00)
_01_ = len(_01)
_11_ = len(_11)
_10_ = len(_10)
if _00_ == k or k == 1:
    print(k)
    for val in d:
        print(val)
elif _00_ + 1 == k:
    print(k)
    for val in d:
        print(val)
elif _01_ > 0 and _10_ > 0:
    print(_00_ + 2)
    for val in _00:
        print(val)
    print(_01[0])
    print(_10[0])
else:
    print(_00_ + 1)
    for val in _00:
        print(val)
    if _01_ > 0:
        print(_01[0])
    elif _10_ > 0:
        print(_10[0])
    elif _11_ > 0:
        print(_11[0])
