(house_len, curtain_len) = map(int, input().split())
if house_len >= curtain_len * 2:
    print(house_len - curtain_len * 2)
else:
    print(0)
