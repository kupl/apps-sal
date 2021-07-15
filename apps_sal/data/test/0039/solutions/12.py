def func(w):
    return w != w[::-1]

word = input().strip()

ss = [word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1) if func(word[i:j])]

print(max(len(w) for w in ss) if ss else 0)

