# バスと電車の組み合わせ運賃の最小値を求める

A = int(input())
B = int(input())
C = int(input())
D = int(input())

fare = [A+C, A+D, B+C, B+D]
print((min(fare)))

