st = input().strip()
st = st[0] + st[2] + st[4] + st[3] + st[1]
st = int(st)**5
st %= 100000
print(str(st).zfill(5))
