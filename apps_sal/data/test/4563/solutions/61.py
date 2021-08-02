n = int(input())
t = [0] * n
a = [0] * n
for i in range(n):
    t[i], a[i] = map(int, input().split())
tcnt = t[0]
acnt = a[0]
for i in range(1, n):
    x = max((tcnt + t[i] - 1) // t[i], (acnt + a[i] - 1) // a[i])
    tcnt = t[i] * x
    acnt = a[i] * x
print(tcnt + acnt)
