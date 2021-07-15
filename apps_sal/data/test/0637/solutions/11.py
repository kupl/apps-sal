n = input()
line = [int(x) for x in input().split()]

current = line[0]
current_size = 1
line_size = -1

for i in line[1:]:
    if i == current:
        current_size = current_size + 1
        if current_size > line_size != -1:
            print("NO")
            return
    if i != current:
        if current_size !=  line_size and line_size!= -1:
            print("NO")
            return
        line_size = current_size
        current = i
        current_size = 1

if current_size != line_size and line_size!= -1:
    print("NO")
    return
print("YES")
