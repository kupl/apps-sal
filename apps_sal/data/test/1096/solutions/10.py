nm = input()
n = nm[0]
m = int(nm[1])
ch = 8
if n == 'a' or n == 'h':
    ch = 5
if m == 1 or m == 8:
    if ch == 8:
        ch = 5
    else:
        ch = 3
print(ch)

