from sys import stdin, stdout
from math import factorial
stdout.write(str(factorial(min(map(int, stdin.readline().split())))))
