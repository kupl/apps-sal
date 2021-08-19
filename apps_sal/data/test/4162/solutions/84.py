N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

# ユークリッドの互除法により最大公約数を求める
ans = 0
val1, val2 = a[0], a[1]
while 1:
    if val1 % val2 == 0:
        ans = a[0] * a[1] // val2
        break
    else:
        tmp = val2
        val2 = val1 % val2
        val1 = tmp

for i in range(2, N):
    val1, val2 = ans, a[i]
    while 1:
        if val1 % val2 == 0:
            ans *= a[i] // val2
            break
        else:
            tmp = val2
            val2 = val1 % val2
            val1 = tmp

f_ans = 0
for i in range(N):
    f_ans += (ans - 1) % a[i]
print((int(f_ans)))
