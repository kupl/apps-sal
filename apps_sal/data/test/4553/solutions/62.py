(a, b) = list(map(int, input().split()))
s = input()
for i in range(a + b + 1):
    if i == a:
        if s[i] != '-':
            print('No')
            break
    elif s[i] == '-':
        print('No')
        break
    elif int(s[i]) < 0 or 9 < int(s[i]):
        print('No')
        break
else:
    print('Yes')
