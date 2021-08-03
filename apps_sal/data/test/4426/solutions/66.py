week = "MON,TUE,WED,THU,FRI,SAT,SUN".split(',')
S = input()
print(7) if S == "SUN" else print(6 - week.index(S))
