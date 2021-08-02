N = int(input())
mns = list(map(int, input().split()))
atk = min(mns)
while 1:
    mns = list(filter(lambda x: x != 0, map(lambda x: x % atk, mns)))
    if not mns:
        break
    mns += [atk]
    atk = min(mns)
print(atk)
