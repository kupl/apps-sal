c = input()
r = 8
if c[0] == 'a' or c[0] == 'h':
    if c[1] == '1' or c[1] == '8':
        r = 3
    else:
        r = 5
if c[1] == '1' or c[1] == '8':
    if c[0] == 'a' or c[0] == 'h':
        r = 3
    else:
        r = 5
print(r)
