n = int(input())
a = input()
k = 1
a = a.lower()
for i in range(97,123):
    if a.count(chr(i)) == 0:
        k=0
        break
if k:
    print("YES")
else:
    print("NO")
