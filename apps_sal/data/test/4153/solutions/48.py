S = input()
 
# 0と1は可能な限り打ち消し合う
c0 = S.count('0')
c1 = S.count('1')

print(2*min(c0, c1))
