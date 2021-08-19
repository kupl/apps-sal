(a, b) = input().split()
(a, b) = (int(a), int(b))
"dic = {\n\t'0': 6,\n\t'1': 2,\n\t'2': 5,\n\t'3': 5,\n\t'4': 4,\n\t'5': 5,\n\t'6': 6,\n\t'7': 3,\n\t'8': 7,\n\t'9': 6\n}"
lst = list(range(a, b + 1))
temp = str(lst)
zero = temp.count('0')
one = temp.count('1')
two = temp.count('2')
three = temp.count('3')
four = temp.count('4')
five = temp.count('5')
six = temp.count('6')
seven = temp.count('7')
eight = temp.count('8')
nine = temp.count('9')
ans = zero * 6 + one * 2 + two * 5 + three * 5 + four * 4 + five * 5 + six * 6 + seven * 3 + eight * 7 + nine * 6
print(ans)
'for i in range(a,b+1):\n\tfor j in str(i):\n\t\tsum += dic[j]\n'
