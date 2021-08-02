# 参考:https://drken1215.hatenablog.com/entry/2020/04/26/193500 #
from math import pi
from math import atan2
a, b, x = map(int, input().split())
x /= a
if x > a * b / 2:
    print(atan2(2 * (a * b - x), (a ** 2)) * 180 / pi)
if x <= a * b / 2:
    print(atan2((b ** 2), 2 * x) * 180 / pi)
