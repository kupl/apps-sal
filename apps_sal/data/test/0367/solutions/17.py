st = input()
arr = [0 for i in range(26)]
ch = 'a'
for i in range(26):
    arr[i] = st.count(chr(i + ord('a')))
i, j = 0, 25
n = len(st)
while i < 26 and arr[i] % 2 == 0:
    i += 1
while j > 0 and arr[j] % 2 == 0:
    j -= 1
while i < j:
    arr[i] = arr[i] + 1
    arr[j] = arr[j] - 1
    while i < 26 and arr[i] % 2 == 0:
        i += 1
    while 0 < j and arr[j] % 2 == 0:
        j -= 1
r = ''
middle = ''

for i in range(26):
    c = str(chr(i + 97))
    r = r + c * (arr[i] // 2)
    if arr[i] % 2 == 1:
        middle = c
print(r + middle + r[::-1])
