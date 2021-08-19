n = int(input())
p = list(map(int, input().split()))
low = 3 * 10 ** 5
cnt = 0
for x in p:
    if x < low:
        cnt += 1
        low = x
print(cnt)
