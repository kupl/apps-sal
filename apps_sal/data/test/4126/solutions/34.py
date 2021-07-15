kaibunkai = input()
n = len(kaibunkai)
zenhan = kaibunkai[:(n-1)//2]
kouhan = kaibunkai[(n+3)//2-1:]


def kaibun_desuka(bun):
  s = len(bun)
  for x in range(s//2):
    if bun[x] != bun[-x-1]:
      return False
  return True

if kaibun_desuka(kaibunkai) and kaibun_desuka(zenhan) and kaibun_desuka(kouhan):
  print("Yes")

  
else:
  print("No")
    

