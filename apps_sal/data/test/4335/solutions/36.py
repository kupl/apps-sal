n = int(input())
s = input()

if n % 2 == 1:
    print('No')
else:
    cnt = 0
    for i in range(0, n // 2):
        cnt += (s[i] == s[i + n // 2])
    if(cnt == n // 2):
        print('Yes')
    else:
        print('No')



