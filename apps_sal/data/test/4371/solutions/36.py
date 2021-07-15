S = input()
S += '0'

num_len = 999
for i in range(len(S)-3):
    X = int(S[i:i+3])
    num_len = min(num_len, abs(753-X))

print(num_len)
