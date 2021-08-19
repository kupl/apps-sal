import numpy
(a, b, x) = list(map(int, input().split()))
if a * b / 2 < x / a:
    theta = numpy.arctan(2 * (b / a - x / a ** 3))
else:
    theta = numpy.arctan(a * b ** 2 / 2 / x)
theta = numpy.rad2deg(theta)
print(theta)
