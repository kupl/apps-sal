n = int(input())
watched = [False] * n
for i in map(int, input().split()):
    watched[i - 1] = True

for i in range(n):
    if not watched[i]:
        print(i + 1)
        break
