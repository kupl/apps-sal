s = input()
if '[' in s and ']' in s and (':' in s):
    e = s.count(':')
    if e < 2:
        print(-1)
    else:
        a = s.index('[')
        b = len(s) - 1 - s[::-1].index(']')
        if b < a:
            print(-1)
        elif s[a + 1:b].count(':') < 2:
            print(-1)
        else:
            st1 = True
            count = 0
            for i in range(a + 1, b):
                if st1 and s[i] == ':':
                    pos1 = i
                    st1 = False
                if s[i] == ':':
                    pos2 = i
            for i in range(pos1 + 1, pos2):
                if s[i] == '|':
                    count += 1
            print(count + 4)
else:
    print(-1)
