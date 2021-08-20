(n, l) = map(int, input().split())
List1 = []
List2 = []
for i in range(n):
    L = l + i
    L_abs = abs(L)
    List1.append(L)
    List2.append(L_abs)
if min(List2) in List1:
    List1.remove(min(List2))
elif -min(List2) in List1:
    List1.remove(-min(List2))
print(sum(List1))
