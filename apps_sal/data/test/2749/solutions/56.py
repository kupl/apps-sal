h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
c = []
for i in range(len(a)):
  c += [i + 1] * a[i]
for i in range(h):
  if i % 2 == 0:
    print((*c[i*w:(i+1)*w]))
  else:
    print((*c[(i+1)*w-1:i*w-1:-1]))

