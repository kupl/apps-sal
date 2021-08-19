(A, B) = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    i = str(i)
    x = len(i) // 2
    left = i[0:x]
    right = i[x + 1:]
    reverse_right = right[::-1]
    if left == reverse_right:
        cnt += 1
print(cnt)
