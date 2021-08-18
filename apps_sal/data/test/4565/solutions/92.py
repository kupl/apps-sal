n = int(input())
s = input()

cnt = s.count('E')

ans = cnt
for i in range(n):
    if s[i] == 'E':
        cnt -= 1
        if ans > cnt:
            ans = cnt

    else:
        cnt += 1

print(ans)
