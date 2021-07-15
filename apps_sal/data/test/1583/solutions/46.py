from math import atan, degrees

def angle(a, b, x):
    return degrees(atan(((a * b ** 2) / ( 2 * x)) if x <= 0.5 * b * a ** 2 else ((2 * (b - (x / (a ** 2)))) / a)))
	
print(angle(*map(int, input().split())))
