S = input()
N = len(S)
words = ['dream', 'dreamer', 'erase', 'eraser']
stack = [0]
ans = "NO"
while stack:
    ind = stack.pop()
    if ind == N:
        ans = 'YES'
        break
    for w in words:
        end = ind + len(w)
        if S[ind:end] == w:
            stack.append(end)
print(ans)
