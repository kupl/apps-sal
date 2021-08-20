(a, b) = list(map(int, input().split()))
s = input()
if len(s) == a + b + 1:
    if s[a] == '-':
        cnt = 0
        for i in range(len(s)):
            if s[i] == '0' or s[i] == '1' or s[i] == '2' or (s[i] == '3') or (s[i] == '4') or (s[i] == '5') or (s[i] == '6') or (s[i] == '7') or (s[i] == '8') or (s[i] == '9'):
                cnt += 1
        if cnt == a + b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
