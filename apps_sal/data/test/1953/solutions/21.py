n = int(input())

times = [int(time) for time in input().split()]
times.sort()

past = 0
ok = 0
for i in range(n):
    if past <= times[i]:
        ok += 1
        past += times[i]

print(ok)
