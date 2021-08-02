[h, m] = [int(x) for x in input().split(':')]
a = int(input())

newm = (m + a) % 60
newh = (h + ((m + a) // 60)) % 24

ans = ''
if (newm < 10 and newh < 10):
    ans = "0{}:0{}".format(newh, newm)
elif (newm < 10):
    ans = "{}:0{}".format(newh, newm)
elif (newh < 10):
    ans = "0{}:{}".format(newh, newm)
else:
    ans = "{}:{}".format(newh, newm)
print(ans)
