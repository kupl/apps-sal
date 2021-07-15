n = int(input())
a = list(int(input()) for _ in range(n))
b = sorted(a, reverse=True)
for i in range(n):
    if a[i] != b[0]:
      print(b[0])
    else: print(b[1])
