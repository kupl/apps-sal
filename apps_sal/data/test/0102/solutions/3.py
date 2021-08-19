inp = input()
n = int(inp)
single = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dec = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
if n < 20:
    print(single[n])
elif n % 10 == 0:
    print(dec[n // 10 - 2])
else:
    print(dec[n // 10 - 2] + '-' + single[int(n % 10)])
