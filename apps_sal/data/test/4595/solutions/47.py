S = input()
s_list = []
for n in S:
    s_list.append(n)

a = (s_list.index("A")) + 1

s_list.reverse()
z = (-(s_list.index("Z") + 1))

print(len(S[a:z]) + 2)
