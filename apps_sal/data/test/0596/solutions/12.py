def isLeep(year):
    if year % 400 == 0:
        return 1;
    else:
        if year % 4 == 0 and year % 100 != 0:
            return 1;
        return 0;
    
def cmp(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        return 0;
    else:
        if y1 == y2 and m1 > m2:
            return 0;
        else:
            if y1 == y2 and m1 == m2 and d1 > d2:
                return 0;
            return 1;

y1, m1, d1 = list(map(int, input().split(':')))
y2, m2, d2 = list(map(int, input().split(':')))

days = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

if cmp(y1, m1, d1, y2, m2, d2) == 0:
    t = y1; y1 = y2; y2 = t;
    t = m1; m1 = m2; m2 = t;
    t = d1; d1 = d2; d2 = t;

res = 0;
while True:
    res = res + 1;
    if y1 == y2 and m1 == m2 and d1 == d2:
        break;
    d1 = d1 + 1;
    if d1 <= days[m1]:
        continue;
    else:
        if d1 == 29:
            if isLeep(y1):
                continue;
            else:
                m1 = 3;
                d1 = 1;
        else:
            if d1 == 30:
                m1 = 3;
                d1 = 1;
            else:
                if d1 == 31:
                    m1 = m1 + 1;
                    d1 = 1;
                else:
                    if d1 == 32:
                        if m1 == 12:
                            y1 = y1 + 1;
                            m1 = 1;
                            d1 = 1;
                        else:
                            m1 = m1 + 1;
                            d1 = 1;

print(res - 1)
            


