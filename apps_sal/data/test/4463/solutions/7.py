s = list(input())
t = list(input())

s.sort()
t.sort(reverse = True)

s1 = ''.join(s)
t1 = ''.join(t)

if s < t :
    print("Yes")
else :
    print("No")

