n = int(input())
s = input()
cnt = 0
if n % 2 == 1:
    print('No')
else:
    for i in range(n // 2):
        if s[i] == s[i + n // 2]:
            cnt += 1
    if cnt == n // 2:
        print('Yes')
    else:
        print('No')
