n = int(input())
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
if n <= 19:
    print(numbers[n])
    return
else:
    if n % 10 == 0:
        print(tens[n // 10])
    else:
        print(tens[n // 10] + '-' + numbers[n % 10])
