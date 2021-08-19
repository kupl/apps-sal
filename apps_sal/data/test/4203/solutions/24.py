S = input()
Ssl = S[2:-1]
Srp = S.replace('A', '')
Srp = Srp.replace('C', '')
cnt = Ssl.count('C')
if S[0] == 'A' and cnt == 1 and Srp.islower():
    print('AC')
else:
    print('WA')
