S = input()
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        print('Bad')
        break
else:
    print('Good')
