def read(): return list(map(int, input().split()))


n = int(input())
a = list(read())
b = [0] * n
j = 0
for i in a:
    if i:
        b[j] = i
        j += 1
cnt = sum(i != 0 for i in b)
for i in range(n):
    if b[i] == 0:
        break
    if b[i] == a[i]:
        cnt -= 1
print(cnt)
