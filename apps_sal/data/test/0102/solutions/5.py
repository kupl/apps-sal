l = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
    'eighteen', 'nineteen', 'twenty'
]

p = [
    'A', 'B',
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety'
]

n = int(input())

if n < len(l):
    print(l[n])
elif n % 10:
    print('%s-%s' % (p[int(n / 10)], l[n % 10]))
else:
    print(p[int(n / 10)])
