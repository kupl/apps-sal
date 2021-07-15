n = int(input())
list_A = list(map(int, input().split()))
m = pow(10, 10)
s = 0
cnt = 1

for a in list_A:
    m = min(m, abs(a))
    if a < 0:
        cnt *= -1
    s += abs(a)

if cnt == 1:
    print(s)
else:
    print(s - 2 * m)
