n = int(input())
s = input()

l = s.split('0')

le = len(l)

ans = 0

for i in range(le):
    t = l[i]
    ans *= 10
    ans += len(t)

print(ans)

