n = int(input())
list_t = list(map(int, input().split()))
list_v = list(map(int, input().split()))

list_v2 = [0 for i in range(n+1)]
list_t.append(0)
list_v.append(0)
for i in range(n-1)[::-1]:
  list_v2[i] = min(list_v[i], list_v[i+1], list_v2[i+1] + list_t[i+1])

dist = 0
v0 = 0
for i in range(n):
  t1 = min(list_v[i] - v0, (list_t[i] - (v0 - list_v2[i])) / 2, list_t[i])
  t2 = max(v0 + t1 - list_v2[i], 0)
  dist += (2*v0+t1)*t1/2 + (v0+t1)*(list_t[i]-t1-t2) + (2*(v0+t1)-t2)*t2/2
  v0 = v0 + t1 - t2
print(dist)
