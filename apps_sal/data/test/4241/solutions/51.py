S = input()
T = input()

num = [0] * len(S) #ここに、被った文字数を格納しておく。リストの中で一番高い数字が、一番多く被っている単語数になる

for i in range(len(S)-len(T)+1):
    for t in range(len(T)):
        if S[i+t] == T[t]:
            num[i] += 1

print(len(T)-max(num))
