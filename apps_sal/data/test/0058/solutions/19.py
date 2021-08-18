_len = int(input())
_ver = int(input())
_up = int(input())
l = [_ver, _ver, _ver, _ver, _up, _up]
l = sorted(l, reverse=True)

n = 1
left = [_len]
for i in range(6):
    for j in range(len(left)):
        if left[j] >= l[i]:
            left[j] -= l[i]
            break
        elif j == len(left) - 1:
            left.append(_len - l[i])
            n += 1
    left = sorted(left)

if n > 2 and _ver * 2 + _up <= _len:
    print(2)
else:
    print(n)
