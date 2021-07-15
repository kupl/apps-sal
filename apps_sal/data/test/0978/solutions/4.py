k = int(input())
panel1 = input()
panel2 = input()
panel3 = input()
panel4 = input()
can = True

for i in range(1,10):
    counter = panel1.count(str(i)) + panel2.count(str(i)) + panel3.count(str(i)) + panel4.count(str(i))
    if counter > k*2 :
        can = False
        break
if can :
    print("YES")
else:
    print("NO")

