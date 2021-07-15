n = int(input())
s =set()
for i in range(n):
    k = input()
    if k in s:
        print("YES")
    else:
        print("NO")
    s.add(k)
