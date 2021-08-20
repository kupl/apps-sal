n = int(input())
l = list(map(int, input().split()))
ans = [1]
b = l[0]
for i in range(1, n):
    if l[i] * 2 <= l[0]:
        b += l[i]
        ans.append(i + 1)
    else:
        b -= l[i]
if b <= 0:
    print(0)
else:
    print(len(ans))
    print(' '.join(map(str, ans)))
