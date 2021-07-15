A, B, T = map(int, input().split())

cnt = 0
while T >= A:
  cnt += B
  T -= A
print(cnt)
