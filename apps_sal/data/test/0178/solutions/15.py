n = int(input())
x = input()

r = (n-11)//2
p = x[:2*r+1]
if p.count("8") >= r+1:
    print("YES")
else:
    print("NO")

