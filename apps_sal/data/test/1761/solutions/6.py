# intent is to get a message with heasts to the fron tand the back.
n=int(input())
words=[]
for _ in range(n):
	words.append(input())
actual = input()
expected = '<3' + '<3'.join(words) + '<3'
le=len(expected)
ie=0
for c in actual:
	if ie<le and c == expected[ie]:
		ie+=1
print('yes' if ie==le else 'no')


