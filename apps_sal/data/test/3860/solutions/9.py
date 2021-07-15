boy = int(input())
girl = int(input())
n = int(input())
cnt = 0
for i in range(0, n + 1):
    j = n - i
    if i <= boy and j <= girl:
        cnt += 1
print(cnt)
