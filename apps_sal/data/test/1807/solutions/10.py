(a, b) = map(int, input().split())
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
