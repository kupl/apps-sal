char = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
(a, b) = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    for f in list(str(i)):
        cnt += char[int(f)]
print(cnt)
