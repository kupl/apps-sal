n, c = list(map(int, input().split()))
a = list(map(int, input().split()))
s = set(a)
k = []
for i in s:
    k.append(a.count(i))
if max(k) % c == 0:
    d = max(k) // c
    d *= c
else:
    d = max(k) // c + 1
    d *= c
result = 0
for i in k:
    result += d - i
print(result)

    

