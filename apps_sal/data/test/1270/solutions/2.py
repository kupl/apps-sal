n = int(input())
ans = []

while n > 3:
    n -= 2
    ans.append(2)

ans.append(n)

print(len(ans))
print(' '.join(map(str, ans)))
