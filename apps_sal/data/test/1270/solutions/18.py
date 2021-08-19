n = int(input())
ans = []
while n > 1:
    if n > 3 or n == 2:
        n -= 2
        ans.append(2)
    else:
        n -= 3
        ans.append(3)
print(len(ans))
print(' '.join((str(i) for i in ans)))
