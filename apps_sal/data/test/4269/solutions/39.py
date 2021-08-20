S = input()
for i in range(0, 3):
    if S[i] == S[i + 1]:
        print('Bad')
        break
else:
    print('Good')
