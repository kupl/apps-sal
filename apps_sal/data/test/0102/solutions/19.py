dec = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
tentotwenty = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
number = int(input())
if number >= 0 and number <= 10:
    print(units[number])
elif number > 10 and number < 20:
    print(tentotwenty[number - 10])
elif number % 10 == 0:
    print(dec[number // 10])
else:
    print(dec[number // 10] + '-' + units[number % 10])
