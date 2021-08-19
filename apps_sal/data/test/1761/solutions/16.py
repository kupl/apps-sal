n = int(input())
text = ''
for _ in range(n):
    temp = input()
    text = text + '<3'
    text = text + temp
text = text + '<3'
tocmp = input()
j = 0
for ch in tocmp:
    if ch == text[j]:
        j += 1
    if j == len(text):
        break
if j == len(text):
    print('yes')
else:
    print('no')
