a, b = map(int, input().split())
c = 1 
cnt = 0 
while c < b:
    c += a-1
    cnt += 1
print(cnt)
