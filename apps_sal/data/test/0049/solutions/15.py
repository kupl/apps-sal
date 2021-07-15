T = (0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889, 1088888888889)
k = int(input())
a = 0
for i in T:
    if i - k > 0:
        a = T.index(i)
        break
temp = T[a] - k
x = temp % a
res = (10 ** a) - 1 - int(temp / a)
ans = int((res % (10 ** (x+1))) / (10 ** x))
print(ans)

