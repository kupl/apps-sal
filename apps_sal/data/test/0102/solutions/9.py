n = int(input())
s = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
s1 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
s2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
if n <= 10:
    print(s[n])
elif n < 20:
    print(s1[n % 10 - 1])
else:
    print(s2[n // 10 - 2], end='')
    if n % 10 != 0:
        print('-', s[n % 10], sep='', end='')
