n = int(input())
home = []
guest = []
switch = 0
for i in range(0, n):
    uniform = str(input())
    guest.append(int(uniform[uniform.index(' ') + 1:]))
    home.append(int(uniform[:uniform.index(' ')]))
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            if home[i] == guest[j]:
                switch += 1
print(switch)
