(h, w) = map(int, input().split())
words = [0] * (h + 2)
for i in range(1, h + 1, 1):
    s = input()
    words[i] = s
for j in range(len(words)):
    if words[j] == 0:
        words[j] = '#' * (w + 2)
    else:
        words[j] = '#' + words[j] + '#'
for ans in words:
    print(ans)
