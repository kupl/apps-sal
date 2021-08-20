n = int(input())
s = input()
sesgsin = []
toksout = []
inparens = []
outparens = []
for (i, c) in enumerate(s):
    if c == '(':
        inparens.append(i)
    elif c == ')':
        outparens.append(i)
numinparen = 0
for (i, o) in zip(inparens, outparens):
    numinparen += sum((1 for t in s[i + 1:o].split('_') if t))
starts = [-1] + outparens
ends = inparens + [len(s)]
maxlen = 0
for (st, e) in zip(starts, ends):
    maxlen = max(maxlen, max((len(t) for t in s[st + 1:e].split('_'))))
print(maxlen, numinparen)
