3

hh, mm = [int(i) for i in input().split(':')]
a = int(input())

mm += a

hh += mm // 60
mm %= 60
hh %= 24

print(str(hh).zfill(2) + ':' + str(mm).zfill(2))

# TODO: Leading zeroes

