n = int(input())
s = input()
s = s.replace('(', '_(_')
s = s.replace(')', '_)_')

word = s.split('_')

cntI = 0
mx = 0
inside = False

for w in word:
    if w == '':
        continue
    # print(w)
    if w == '(':
        inside = True
        continue
    if w == ')':
        inside = False
        continue

    if inside:
        cntI += 1
    else:
        mx = max(mx, len(w))

print(mx, cntI)
