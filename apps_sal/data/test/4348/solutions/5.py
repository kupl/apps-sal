import string
from collections import Counter
(n, k) = [int(i) for i in input().split()]
s = input()
counter = Counter(s)
for char in string.ascii_lowercase:
    delta = min(k, counter[char])
    k -= delta
    counter[char] -= delta
s2 = ''
for char in s[::-1]:
    if counter[char] > 0:
        s2 += char
        counter[char] -= 1
print(s2[::-1])
