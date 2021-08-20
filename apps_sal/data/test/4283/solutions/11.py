n = input()
n = int(n)
a = input()
a = [int(i) for i in a.split()]
a.sort()
_min = 0
_max = 0
_dict = {}
for i in a:
    if _min < i - 5:
        _max = max(_max, sum(_dict.values()))
        _dict = {key: value for (key, value) in _dict.items() if key >= i - 5}
    _dict[i] = _dict[i] + 1 if i in _dict else 1
_max = max(_max, sum(_dict.values()))
print(_max)
