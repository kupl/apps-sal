S = input()

left = -1

for i,s in enumerate(S):
    if s == 'A':
        left = i
        break

right = len(S)+1
for i in range(len(S)-1, -1, -1):
    if S[i] == 'Z':
        right = i
        break

if left < right:
    print(right-left+1)
