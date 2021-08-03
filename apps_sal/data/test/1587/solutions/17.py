n = int(input())
c = input()
cnt = [0 for _ in range(n)]
red = 0
for i in range(n):
    if c[i] == 'R':
        red += 1
    cnt[i] = red

print(red - cnt[red - 1])
