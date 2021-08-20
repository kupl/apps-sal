(A, B) = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    l = list(str(i))
    if l[0] == l[4] and l[1] == l[3]:
        cnt += 1
print(cnt)
