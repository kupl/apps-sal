n = int(input())
ans = 0
a = ''
l = []
for i in range(n):
    w = input()
    if a == w[0]:
        ans += 1
    a = w[-1]
    l.append(w)
x = 'No'
if ans == n-1 and len(set(l)) == n:
    x = 'Yes'
print(x)
