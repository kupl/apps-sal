n = int(input())
rates = map(int, input().split())
colors = set()
over = 0
for rate in rates:
    if 1 <= rate and rate <= 399:
        colors.add('1-399')
    if 400 <= rate and rate <= 799:
        colors.add('400-799')
    if 800 <= rate and rate <= 1199:
        colors.add('800-1199')
    if 1200 <= rate and rate <= 1599:
        colors.add('1200-1599')
    if 1600 <= rate and rate <= 1999:
        colors.add('1600-1999')
    if 2000 <= rate and rate <= 2399:
        colors.add('2000-2399')
    if 2400 <= rate and rate <= 2799:
        colors.add('2400-2799')
    if 2800 <= rate and rate <= 3199:
        colors.add('2800-3199')
    if 3200 <= rate:
        over += 1
min = len(colors)
max = min + over
if min == 0:
    min = 1
print(min, max)
