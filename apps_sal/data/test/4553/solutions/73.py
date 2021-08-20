(a, b) = map(int, input().split())
s = input()
num = '0123456789'
if all((s[i] in num for i in range(a))) and s[a] == '-' and all((s[-(i + 1)] in num for i in range(b))):
    print('Yes')
else:
    print('No')
