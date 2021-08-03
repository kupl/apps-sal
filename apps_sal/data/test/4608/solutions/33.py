N = int(input())
a = []

for _ in range(N):
    a.append(int(input()) - 1)

i, count = 0, 0
success = False
for _ in range(N):
    i = a[i]
    count += 1

    if i == 1:
        success = True
        break

if not success:
    count = -1

print(count)
