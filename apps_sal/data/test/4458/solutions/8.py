n = int(input())
a = list(map(int, input().split()))

cnt = 0
mina = a[0]

for i in a:
    if i <= mina:
        cnt += 1
        mina = i

print(cnt)
