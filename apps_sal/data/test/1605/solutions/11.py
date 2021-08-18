'''input
babaa
'''
from sys import stdin


string = list(stdin.readline().strip())
odd_a = 0
even_a = 0
odd_b = 0
even_b = 0
even = 0
odd = 0

for i in string:
    if i == 'a':
        temp = odd_a
        odd_a = even_a + 1
        even_a = temp
        even_b, odd_b = odd_b, even_b
        odd += odd_a
        even += even_a
    else:
        temp = odd_b
        odd_b = even_b + 1
        even_b = temp
        even_a, odd_a = odd_a, even_a
        odd += odd_b
        even += even_b
print(even, odd)
