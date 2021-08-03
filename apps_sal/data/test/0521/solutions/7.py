n = int(input())
s = input()

if ((s.find('??') >= 0 or s[0] == '?' or s[-1] == '?'
    or any(s.find(c + '?' + c) >= 0 for c in ['C', 'M', 'Y'])) and
        all(s.find(x) < 0 for x in ['CC', 'MM', 'YY'])):
    print("Yes")
else:
    print("No")
