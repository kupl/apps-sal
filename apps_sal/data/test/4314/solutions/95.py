h,w = map(int, input().split())
a0 = [[] for i in range(h)]
for i in range(h):
  a0[i] = input()
a = [j for j in a0 if "#" in j]
at0 = list(map(list, zip(*a)))
for k in range(len(at0)):
  at0[k] = "".join(at0[k])
at = [l for l in at0 if "#" in l]
for m in list(map(list, zip(*at))):
  print("".join(m))
