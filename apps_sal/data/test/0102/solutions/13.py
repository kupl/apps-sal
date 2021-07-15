digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
a1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def word(s):
	if s in range(10):
		return digits[s]
	elif s in range(20):
		return a1[s - 10]
	elif s % 10 == 0:
		return decades[s // 10 - 1]
	else:
		return decades[s // 10 - 1] + '-' + digits[s % 10]


s = int(input())
print(word(s))



