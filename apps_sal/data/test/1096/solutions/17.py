cd = input()
if cd[0] != 'a' and cd[0] != 'h':
    if cd[1] != '1' and cd[1] != '8':
        print(8)
    else:
        print(5)
elif cd[1] != '1' and cd[1] != '8':
    print(5)
else:
    print(3)
