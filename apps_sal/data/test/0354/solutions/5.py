s = input()
t = input()
vowels = 'aeiou'
if len(s) != len(t):
    print('No')
else:
    for i in range(len(s)):
        if (s[i] in vowels) ^ (t[i] in vowels):
            print('No')
            break
    else:
        print('Yes')
