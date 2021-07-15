S = input()
S_ = S[::-1]

count = 0
for i in range(len(S)//2):
    if S[i] != S_[i]:
        count += 1
print(count)
