# [0] == [1] or [1] == [2] or [2] == [3]だとBad

S = list(input())
# print(S[0])

if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print('Bad')
else:
    print('Good')
