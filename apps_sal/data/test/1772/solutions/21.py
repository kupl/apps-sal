n = int(input())
mas = list(map(int, input().split()))
r1 = [i for i in mas if i % 2 == 0]
r2 = [i for i in mas if i % 2 != 0]
r1 = len(r1)
r2 = len(r2)
if min(r1, r2) == r2:
    k = r2
else:
    k = r1 + ( (r2 - r1) //3)
print(k)
