import math
k = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
n = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
a = int(input())
if a < 20:
    a = k[a]
else:
    a = n[a // 10] + k[a % 10]
b = 'k' in a or 'a' in a or 'n' in a
print('NO' if b else 'YES')
