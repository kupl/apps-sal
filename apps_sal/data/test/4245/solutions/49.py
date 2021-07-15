A, B = map(int, input().split())

outlet = 1
cnt = 0
while outlet < B:
  outlet += A - 1
  cnt += 1
print(cnt)
