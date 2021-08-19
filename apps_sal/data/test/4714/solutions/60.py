(A, B) = list(map(int, input().split()))
cnt = 0
for num in range(A, B + 1):
    num = list(str(num))
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            break
    else:
        cnt += 1
print(cnt)
