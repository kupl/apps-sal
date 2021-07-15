S = str(input())
saishou = 1000

for i in range(len(S)-2):
    SS = int(S[i]+S[i+1]+S[i+2])
    if abs(753-SS) < saishou:
        saishou = abs(753-SS)

print(saishou)
