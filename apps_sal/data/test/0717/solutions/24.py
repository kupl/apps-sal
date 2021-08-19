n = int(input())
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > cnt:
        cnt = a
    else:
        cnt = cnt - (cnt - a) % b + b
    # print(cnt)
print(cnt)
