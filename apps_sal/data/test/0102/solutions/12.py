num2words1 = {0:'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
			6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
			11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
			15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
num2words2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number(Number):
	if 0 <= Number <= 19:
		return num2words1[Number]
	elif 20 <= Number <= 99:
		tens, below_ten = divmod(Number, 10)
		s = num2words2[tens - 2]
		if below_ten != 0:
			s += '-'+num2words1[below_ten]
		return s

	

def main():
	t = int(input())
	print(number(t))



def __starting_point():
	main()    

__starting_point()
