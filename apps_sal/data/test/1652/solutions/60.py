S = input()
d = ['dream', 'dreamer', 'erase', 'eraser']
d = [i[::-1] for i in d]

S = S[::-1]
i = 0
while i < len(S):
    ok = False
    for j in d:
        if S[i:i + len(j)] == j:
            i += len(j)
            ok = True
            break
    if ok is False:
        print("NO")
        import sys
        return

print("YES")

