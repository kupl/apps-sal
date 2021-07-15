def digit6(n):
  return ("000000" + str(n))[-6:]

def main():
  N, M = list(map(lambda n: int(n), input().split(" ")))
  CITY = []
  for i in range(M):
    tmp = input().split(" ")
    CITY.append({
      "pref": int(tmp[0]),
      "year": int(tmp[1]),
      "no": i + 1
    })
    
  CITY.sort(key=lambda c: (c["pref"], c["year"]))
  
  order = 0
  pref = ""
  for c in CITY:
    if pref != c["pref"]:
      pref = c["pref"]
      order = 1
    else:
      order += 1
    c["id"] = digit6(pref) + digit6(order)
  
  CITY.sort(key=lambda c: c["no"])
  for i in range(len(CITY)):
    print(CITY[i]["id"])
      
    
  
main()
