n = int(input())
a = [ord(c) - 97 for c in input()]
b = [ord(c) - 97 for c in input()]
ans = []
p = n - 1
bemp = b[p] + a[p]
while p > 0:
    p -= 1
    bemp += (b[p] + a[p]) * 26
    ans.append(chr(int(bemp / 2) % 26 + 97))
    bemp //= 26
ans.append(chr(int(bemp / 2) % 26 + 97))
p = n
while p:
    p -= 1
    print(ans[p], end='')
