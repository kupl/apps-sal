tkhp, tkat, aohp, aoat = map(int, input().split())

while True:
    aohp -= tkat
    if aohp <= 0:
        print("Yes")
        break

    tkhp -= aoat
    if tkhp <= 0:
        print("No")
        break
