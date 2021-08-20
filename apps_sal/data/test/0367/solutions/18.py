import string
s = input()
freq = {x: 0 for x in string.ascii_lowercase}
for char in s:
    freq[char] += 1
head = 'a'
tail = 'z'
while head < tail:
    if freq[tail] % 2 == 0:
        tail = chr(ord(tail) - 1)
        if tail <= head:
            break
    if freq[head] % 2 == 0:
        head = chr(ord(head) + 1)
        if tail <= head:
            break
    if freq[head] % 2 != 0 and freq[tail] % 2 != 0:
        freq[head] += 1
        freq[tail] -= 1
middle_letter = None
if head == tail and freq[head] % 2 != 0:
    middle_letter = head
    freq[head] -= 1
output = ''
for x in string.ascii_lowercase:
    for i in range(freq[x] // 2):
        output += x
if middle_letter:
    output += middle_letter + output[::-1]
else:
    output += output[::-1]
print(output)
