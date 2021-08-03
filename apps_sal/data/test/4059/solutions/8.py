N = int(input())
cnt = 0
for i in range(1, N):
    add = (N - 1) // i
#  print(add)
    cnt += add
    if add < 1:
        break

print(cnt)
