k = int(input())
num = [int(i) for i in input()]


num.sort()
q = k - sum(num)
w = 0
while q > 0:
    q -= 9 - num[w]
    w += 1
print(w)
