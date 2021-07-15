a = input()
b = input()
digits = list(a)
builder=''
if len(b)<len(a):
	b = b.rjust(len(a), '0')
for digit in b:
	if len(b)>len(a):
		break
	if digit in digits:
		digits.remove(digit)
		if int(builder+digit+''.join(sorted(digits, key=int)))<=int(b):
			builder += digit
			continue
		else:
			digits.append(digit)
	added = max([d for d in digits if d<digit])
	builder += added
	digits.remove(added)
	break
builder += ''.join(sorted(digits, reverse=True, key=int))
print(builder)
