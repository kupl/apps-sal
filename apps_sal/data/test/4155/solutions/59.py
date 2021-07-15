n = int(input())
h = list(map(int, input().split()))
H = [h]
ans = 0
while len(H) > 0:
  for e in H:
    if len(e) == 0:
      H.remove(e)
    elif 0 in e:
      a = e[:e.index(0)]
      b = e[e.index(0) + 1:]
      H.append(a)
      H.append(b)
      H.remove(e)
      if [] in H:
        H.remove([])
        if len(H) == 0:
          break
    else:
      ans += min(e)
      c = [e[j] - min(e) for j in range(len(e))]
      a = c[:c.index(0)]
      b = c[c.index(0) + 1:]
      H.append(a)
      H.append(b)
      H.remove(e)
      if [] in H:
        H.remove([])
        if len(H) == 0:
          break
    if [] in H:
      H.remove([])
      if len(H) == 0:
        break
print(ans)
