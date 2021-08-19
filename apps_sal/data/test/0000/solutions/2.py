s = input()
if '[' in s:
    s = s[s.find('[') + 1:]
    if ']' in s:
        s = s[:s.rfind(']')]
        if s.count(':') >= 2:
            s = s[s.find(':') + 1:s.rfind(':')]
            print(s.count('|') + 4)
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)
