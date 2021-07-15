S = input()
for i in range(2, len(S), 2):
    end = len(S)-i
    center = int(end/2)
    if S[:center] == S[center:end]:
        print(end)
        break
