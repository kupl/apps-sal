n,a,x,b,y = map(int,input().split())

t_a = [a]
current = a
while current != x:
    current += 1
    if current == (n+1):
        current = 1
    t_a.append(current)

t_b = [b]
current = b
while current != y:
    current -= 1
    if current == 0:
        current = n
    t_b.append(current)
steps = min(len(t_a),len(t_b))

for i in range(steps):
    if t_a[i] == t_b[i]:
        print ("YES")
        return
print ("NO")
