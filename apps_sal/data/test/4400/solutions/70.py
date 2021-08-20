S = input()
if 'R' in S[0] == 'R' in S[1] == 'R' in S[2]:
    print(3)
elif 'R' in S[0] == 'R' in S[1] or 'R' in S[1] == 'R' in S[2]:
    print(2)
elif 'R' in S[0] or 'R' in S[1] or 'R' in S[2]:
    print(1)
else:
    print(0)
