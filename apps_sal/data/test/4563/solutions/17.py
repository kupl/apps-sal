import math
from fractions import Fraction
n = int(input())
# t0, a0 = map(int, input().split())
anst = 1
ansa = 1
for _ in range(n):
    ti, ai = list(map(int, input().split()))
    anst = ti * math.ceil(max(Fraction(anst, ti), Fraction(ansa, ai)))
    ansa = ai * math.ceil(max(Fraction(anst, ti), Fraction(ansa, ai)))
    # p
    # if math.ceil(anst/ti) < math.ceil(ansa/ai):
    #     # if math.ceil(anst/ti)*ai >= ansa:
    #     #     anst = ti * math.ceil(anst/ti)
    #     #     ansa = ai * math.ceil(anst/ti)
    #     # else:
    #     ansa = ai * math.ceil(ansa/ai)
    #     anst = ti * math.ceil(ansa/ai)
    # else:
    #     # if math.ceil(ansa/ai)*ti >= anst:
    #     #     ansa = ai * math.ceil(ansa/ai)
    #     #     anst = ti * math.ceil(ansa/ai)
    #     # else:
    #     ansa = ai * math.ceil(anst/ti)
    #     anst = ti * math.ceil(anst/ti)
    # # print("anst", anst,"ansa = ", ansa)

print((int(anst + ansa)))
