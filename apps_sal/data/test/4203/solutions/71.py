s = input()
answer = 'WA'
if s[0] == 'A':
    if s.count('C',2,len(s) - 1) == 1:
        a = s.index('C')
        t = s[1:a] + s[a + 1:]
        if t.islower():
            answer = 'AC'
            
print(answer)
