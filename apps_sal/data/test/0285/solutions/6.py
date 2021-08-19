n = int(input())
done = False
(a, b) = map(int, input().split())
a += 1 / 4000000
b -= 1 / 4000000
lol = []
wow = []
for i in range(n):
    (k, c) = map(int, input().split())
    lol.append([k * a + c, i])
    wow.append([k * b + c, i])
wow.sort()
lol.sort()
for i in range(n):
    if lol[i][1] != wow[i][1]:
        print('YES')
        done = True
        break
if not done:
    print('NO')
