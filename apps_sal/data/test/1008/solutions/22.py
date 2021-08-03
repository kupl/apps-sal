s = input()
k = int(input())
leng = len(s) // k
ans = 'YES'
if len(s) % k != 0:
    ans = 'NO'
for i in range(k):
    a = s[i * leng: (i + 1) * leng]
    if a != a[::-1]:
        ans = 'NO'
print(ans)
