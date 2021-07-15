n = int(input())
b = [int(i) for i in input().split()]
prev = b[0]
cnt = 0
for i in b:
    cnt += min(i, prev)
    prev = i
cnt += b[-1]
print(cnt)


