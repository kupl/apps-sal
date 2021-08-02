num = int(input())
dec = num // 10
s = ''
low = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
high = ['__0', '__1', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
if dec > 1:
    s = high[dec]
    if num % 10 != 0:
        print(s + '-' + low[num % 10])
    else:
        print(s)
else:
    print(low[num])
