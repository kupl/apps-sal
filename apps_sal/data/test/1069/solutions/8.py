__author__ = 'nikolay'
s = input()
d = int(s[-2:]) % 4
two = [1, 2, 4, 3]
three = [1, 3, 4, 2]
four = [1, 4]
ans = (1 + two[d] + three[d] + four[d % 2]) % 5
print(ans)
