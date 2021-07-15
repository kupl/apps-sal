S = input()

# 0と1が可能な限り打ち消しあう様を想像せよ
c0 = S.count('0')
c1 = S.count('1')
print(2*min(c0, c1))
