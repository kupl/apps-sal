import sys
s = sys.stdin.readline().strip()
hash = [0] * 256
for ch in s:
    hash[ord(ch) - 97] += 1
count = 0
for i in range(256):
    count += 1 if hash[i] % 2 != 0 else 0
if count == 0 or count % 2 != 0:
    print('First')
else:
    print('Second')
