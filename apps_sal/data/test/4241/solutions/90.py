S = input()
T = input()

# 仮の答え
answer = len(S)


def calculate_difference(word_s, word_t):
    return sum([0 if word_s[i] == word_t[i] else 1
                for i in range(len(word_s))])


# S の何文字目にTを重ねるか
for s_index in range(0, len(S) - len(T) + 1):
    s_substring = (S[s_index: s_index + len(T)])
    answer = min(answer, calculate_difference(s_substring, T))

print(answer)
