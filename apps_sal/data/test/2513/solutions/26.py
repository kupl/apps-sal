d = {"WWo": "S",
     "WSo": "W",
     "SWo": "W",
     "SSo": "S",
     "WWx": "W",
     "WSx": "S",
     "SWx": "S",
     "SSx": "W",
    }

combo = ["SS","SW","WS","WW"]

N = int(input())
z = input()

matched = False
txt = []
for c in combo:
  keep = c[0]
  left = c
  txt = []
  for i in range(N):
    txt.append(left[1])
    new_ch = d[left+z[i]]
    left = left[1] + new_ch
  if left == c:
    matched = True
    break

if matched:
  print(*txt,sep="")
else:
  print("-1")
