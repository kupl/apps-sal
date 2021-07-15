n, s = map(int, input().split())
buys = dict()
sell = dict()
for _ in range(n):
  f = input().split()
  if (f[0] == "B"):
    buys[int(f[1])] = buys.get(int(f[1]), 0) + int(f[2])
  else:
    sell[int(f[1])] = sell.get(int(f[1]), 0) + int(f[2])
bres = sorted(buys.keys(), reverse = True)
sres = sorted(sell.keys())
if bres:
  bs = bres[min(s - 1, len(bres) - 1)]
if sres:
  ss = sres[min(s - 1, len(sres) - 1)]
  for key in sorted(sell.keys(), reverse = True):
    if (key <= ss):
      print("S", key, sell[key])
if bres:
  bs = bres[min(s - 1, len(bres) - 1)]
  for key in sorted(buys.keys(), reverse = True):
    if (key >= bs):
      print("B", key, buys[key])
