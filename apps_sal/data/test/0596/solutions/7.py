from datetime import date,timedelta
import sys

def get_input ():
  return list(map (int,input().split(':')))

sy,sm,sd = get_input()
ey,em,ed = get_input()

#start = date (sy,sm,sd)
#end = date (ey,em,ed)

end = date (sy,sm,sd)
start = date (ey,em,ed)

print(abs((end-start).days))

