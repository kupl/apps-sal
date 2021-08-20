x = int(input().strip())
first_line = input().strip()
hh = first_line.split()[0]
mm = first_line.split()[1]
num_snooze = 0
while '7' not in hh and '7' not in mm:
    h = int(hh)
    m = int(mm)
    m -= x
    if m < 0:
        m += 60
        h -= 1
        if h < 0:
            h += 24
    num_snooze += 1
    hh = str(h)
    mm = str(m)
print(num_snooze)
