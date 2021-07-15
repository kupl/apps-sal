n = int(input())

BASE = 2400

answer = False

for i in range(n):
    before, after = list(map(int, input().split()[1:3]))

    if before >= BASE and after - before > 0:
        answer = True
        break

print("YES" if answer else "NO")

